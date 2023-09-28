import subprocess
import pdb
import logging
import os
from contextlib import contextmanager
import requests
import stat


class InstallUtil:
    def __init__(self, debug=False, log=True, dry=False) -> None:
        self.debug = debug
        self.log = log
        self.dry = dry
        self.file_path = os.path.dirname(os.path.realpath(__file__))
        self.nrs_root = os.path.dirname(self.file_path)

    @contextmanager
    def dir_context(self, path):
        if not os.path.exists(path):
            raise RuntimeError(f"path {path} does not exist")
        cwd = os.getcwd()
        try:
            os.chdir(path)
            yield path
        finally:
            os.chdir(cwd)

    def get_clone_path(self, url):
        name = os.path.basename(url).split(".")[0]
        return os.path.join(self.nrs_root, "env", name)

    def exec_shell(self, cmd):
        output = None
        if self.log:
            logging.info(f'Executing Command "{cmd}" in shell, at {os.getcwd()}')
        # Set breakpoint before potential exception
        if self.debug:
            pdb.set_trace()
        if not self.dry:
            output = subprocess.check_output(cmd, shell=True)
        return output

    def git_clone(self, url, dest):
        if os.path.exists(dest):
            cmd = "git pull"
            with self.dir_context(dest):
                return self.exec_shell(cmd)
        else:
            cmd = f"git clone {url} {dest}"
            return self.exec_shell(cmd)

    def bootstrap(self, wd, cmd="./bootstrap"):
        with self.dir_context(wd):
            return self.exec_shell(cmd)

    def preconfig(self, wd):
        cmd = "./Util/preconfig"
        with self.dir_context(wd):
            return self.exec_shell(cmd)

    def configure(self, wd):
        cmd = f'./configure --prefix={os.path.join(self.nrs_root, "env")}'
        with self.dir_context(wd):
            return self.exec_shell(cmd)

    def make(self, wd):
        cmd = "make -j`nproc`"
        with self.dir_context(wd):
            return self.exec_shell(cmd)

    def make_install(self, wd):
        cmd = "make install"
        with self.dir_context(wd):
            return self.exec_shell(cmd)

    def link(self, src, dest):
        if not os.path.exists(src):
            raise ValueError("Provided source path does not exist")

        if os.path.islink(dest):
            os.unlink(dest)
        else:
            if os.path.exists(dest):
                import shutil

                shutil.rmtree(dest)
        os.symlink(src, dest)

    def wget(self, url, dest):
        r = requests.get(url)
        open(dest, "wb").write(r.content)
        os.chmod(dest, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)


def installer(f, *args, **kwargs):
    def install(*args, **kwargs):
        logging.info(f"Installing {f.__name__}")
        try:
            f(*args, **kwargs)
        except Exception as inst:
            logging.error(f"{f.__name__} install failed")
            print(inst)
        logging.info(f"{f.__name__} success")

    return install


def standard_clone(url):
    repo_dir = util.get_clone_path(url)
    util.git_clone(url, repo_dir)
    return repo_dir


def standard_build(util, wd):
    util.configure(wd)
    util.make(wd)
    util.make_install(wd)

@installer
def help2man(util: InstallUtil):
    url = "http://mirrors.ocf.berkeley.edu/gnu/help2man/help2man-1.49.3.tar.xz"
    dl_path = os.path.join(util.nrs_root, "env", os.path.basename(url))
    util.wget(url, dl_path)
    util.exec_shell(f'tar -xf {dl_path}')
    repo_dir = os.path.join(util.nrs_root, "env", "help2man-1.49.3")
    standard_build(util, repo_dir)


@installer
def autoconf(util: InstallUtil):
    repo_dir = standard_clone("http://git.sv.gnu.org/r/autoconf.git")
    util.bootstrap(repo_dir)
    standard_build(util, repo_dir)


@installer
def zplug(util: InstallUtil):
    standard_clone("https://github.com/zplug/zplug.git")


@installer
def neovim(util: InstallUtil):
    url = "https://github.com/neovim/neovim/releases/latest/download/nvim.appimage"
    repo_dir = util.get_clone_path(url)
    util.wget(url, repo_dir)
    util.link(repo_dir, f"{util.nrs_root}/env/bin/nvim")


@installer
def lazyvim(util: InstallUtil):
    repo_dir = standard_clone("https://github.com/LazyVim/starter")
    repo_dir = util.nrs_root + "/env/starter"
    util.link(repo_dir, os.path.expanduser("~") + "/.config/nvim")


# @installer
# def nerd_fonts(util: InstallUtil):
    # repo_dir = standard_clone("https://github.com/ryanoasis/nerd-fonts.git")
    # url = 'https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Meslo.zip'
    # repo_dir = util.get_clone_path(url)
    # util.wget(url, repo_dir)

    # util.exec_shell(f"{repo_dir}/install.sh Meslo")
    


@installer
def htop(util: InstallUtil):
    repo_dir = standard_clone("https://github.com/htop-dev/htop.git")
    util.bootstrap(repo_dir, "./autogen.sh")
    standard_build(util, repo_dir)


@installer
def fzf(util: InstallUtil):
    repo_dir = standard_clone("https://github.com/junegunn/fzf.git")
    util.link(repo_dir, os.path.expanduser("~") + "/.fzf")
    util.exec_shell(f"{repo_dir}/install --all")


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        level=logging.INFO,
    )
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", dest="debug", action="store_true")
    parser.add_argument("-l", "--log", dest="log", action="store_true")
    parser.add_argument("-t", "--dry", dest="dry", action="store_true")

    args = parser.parse_args()
    util = InstallUtil(debug=args.debug, log=args.log, dry=args.dry)

    # Installing dependencies
    help2man(util)
    autoconf(util)
    zplug(util)
    neovim(util)
    lazyvim(util)
    # nerd_fonts(util)
    fzf(util)
