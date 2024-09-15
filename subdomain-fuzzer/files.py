# This file is part of [osint-tools]. 
# # [osint-tools] is free software: you can redistribute it and/or 
# # modify it under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at your option) 
# any later version. 
# # [osint-tools] is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details. 
# # You should have received a copy of the GNU General Public License 
# # along with [osint-tools]. If not, see <http://www.gnu.org/licenses/>.



import asyncio



class Wordlist:
    def __init__(self, wordlist_file):
        self.wordlist_file = wordlist_file
   
    def read_wordlist(self):
        try:
            with open(f"{self.wordlist_file}", "r") as wl:
                list_subdom = wl.read().split("\n")
                return list_subdom
        except FileNotFoundError:
            print("ERROR : cannot find the file")



class OutputFile:
    def __init__(self, output_file="output.txt"):
        self.output_file = output_file
    
    def create_file(self):
        with open(self.output_file, "w") as f:
            pass

    async def add_file(self, obj_fuzzer):
        with open(self.output_file, "w") as f:
            for val in obj_fuzzer.links:
                f.write(val+"\n")



if __name__ == "__main__":
    pass
