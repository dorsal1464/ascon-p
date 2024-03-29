#!/usr/bin/python3

from scipy.io import savemat
from matplotlib import pyplot as plt
import argparse
import subprocess
import os

cwd = os.getcwd()
linuxwd = "/mnt/"+cwd.replace('\\', '/').replace("C:", "c")
usuba_funcs = {"isw_mult":0, "Sbox__V64":0, "AddConstant__V64":0, "LinearLayer__V64":0, "ascon12":0}
gen_funcs = {"dS_AND":0, "dS_UMA_AND":0, "dS_ROUND":0 }

parser = argparse.ArgumentParser(description='Codesize of various implementations of ISAP permutation block.')
parser.add_argument('--arch', choices=['x86', 'x64', 'armv7', 'aarch64'], default=['x64'], nargs=1, help='compile for 32/64 bit; compile for armv7/aarch64;')
parser.add_argument('--maskrange', type=int, default=[2, 2], nargs=2, metavar='N', help='masking order range')
parser.add_argument('-v', help='verbose', action='store_true')

nmsp = vars(parser.parse_args())
p = nmsp['arch'][0]
drange = nmsp['maskrange']
verbose = nmsp['v']
uma_str = ""

if verbose:
    print(f"{p} arch...")

y1, y2 = [[], []]

for d in range(drange[0], drange[1]+1):
    with open(cwd+"\\globals.h", "r") as f:
        s = f.read().split('\n')
        if "#define REFRESH_ISW" in s:
            refresh_str = "_REFRESH_ISW_20"
        if "#define REFRESH_HPC" in s:
            refresh_str = "_REFRESH_HPC_20"
        s[0] = f"#define MASKING_ORDER {d}"
        s = '\n'.join(s)
        with open(cwd+"\\globals.h", "w") as f:
            f.write(s)
        if p in ['x86', 'x64']:
            os.system(f"wsl make")
        elif p=='aarch64':
            os.system(f"wsl make aarch64")
        elif p=='armv7':
            os.system(f"wsl make armv7")

    c_output = subprocess.run(["wsl", "nm", "-S", f"{linuxwd}/bin_{p}/main_{p}"], capture_output=True)
    stdout = c_output.stdout.decode().split('\n')
    for line in stdout:
        func = line.split(" ")[-1]
        for sig in usuba_funcs.keys():
            if func.find(sig) != -1:
                size = int(line.split(" ")[-3], 16)
                usuba_funcs[sig] = size
                if verbose:
                    print(f"{sig}: {size}")
        for sig in gen_funcs.keys():
            if func.find(sig) != -1:
                size = int(line.split(" ")[-3], 16)
                gen_funcs[sig] = size
                if verbose:
                    print(f"{sig}: {size}")
    if p in ['x86', 'x64']:
        usuba_funcs["LinearLayer__V64"] = 0
    #         or 74 or 100
    y1.append(130+1*(gen_funcs["dS_ROUND"]+1*gen_funcs["dS_AND"]+1*gen_funcs["dS_UMA_AND"]))
    if verbose:
        print(f"generic C codesize(d={d}): ", y1[-1])
    # y2.append(usuba_funcs["ascon12"]+12*(usuba_funcs["AddConstant__V64"]+usuba_funcs["Sbox__V64"]+usuba_funcs["LinearLayer__V64"]+5*usuba_funcs["isw_mult"]))
    y2.append(usuba_funcs["ascon12"]+1*(usuba_funcs["Sbox__V64"]+usuba_funcs["LinearLayer__V64"]+1*usuba_funcs["isw_mult"]))
    if verbose:
        print(f"usuba codesize(d={d}): ", y2[-1])

x = list(range(drange[0], drange[1]+1))
print("---->")
print(f"{x=}")
print(f"{y1=}")
print(f"{y2=}")
plt.title(f"Codesize - {p}")
plt.plot(x, y1, x, y2)
plt.show()
savemat(f"{cwd}\\results\\codesize_{p}{uma_str}.mat", {"d": x, "gc": y1, "uc": y2})
