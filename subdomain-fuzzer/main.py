#!/usr/bin/env python3



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



from files import Wordlist, OutputFile
from fuzzer import Fuzzer
import asyncio
import aiohttp
import sys



def flag_handler():
    print(sys.argv)
    args = sys.argv[1::]
    
    default_args = {
        "url": "owasp-juice.shop",
        "wordlist": "wordlist.txt",
        "status": "200,302,403",
        "output": "output.txt"
    }
    
    if not args:
        print('TRY TO INPUT SMTH LIKE THIS: ./subdomain-fuzzer.sh url=owasp-juice.shop wordlist=wordlist.txt status=200,302,403 output=output.txt', sep='\n')
        print('Arguments were not set! Using default values:')
        for key, value in default_args.items():
            print(f"{key} = {value}")
        return default_args
    else:
        user_args = dict(arg.split('=') for arg in args)
        default_args.update(user_args)
        return default_args



async def main():
    try:
        dict_flag = flag_handler()

        wlst = Wordlist(wordlist_file=dict_flag["wordlist"])
        fzzr = Fuzzer(target_url=dict_flag["url"], status_codes=dict_flag["status"])
        otpt = OutputFile(output_file=dict_flag['output'])

        lst_wlst = wlst.read_wordlist()
        otpt.create_file()

        await fzzr.send_requests(lst_wlst)
        await otpt.add_file(fzzr)

    except KeyError:
        print('TRY TO INPUT SMTH LIKE THIS: ./subdomain-fuzzer url=owasp-juice.shop wordlist=wordlist.txt status=200,302,403 output=output.txt', sep='\n')



if __name__ == "__main__":
    asyncio.run(main())
