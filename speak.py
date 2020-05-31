#coding:utf-8
import subprocess

word = input("input::")
print("say:"+word)

subprocess.getstatusoutput("ilang '" + word + "'")