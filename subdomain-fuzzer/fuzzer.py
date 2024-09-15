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
import aiohttp



class Fuzzer:
    def __init__(self, target_url, status_codes=[200, 302, 403]):
        self.target_url = target_url
        self.status_codes = status_codes
        self.client_session = None
        self.links = []

    async def send_requests(self, wordlist_file):
        async with aiohttp.ClientSession() as session:
            for sub in wordlist_file:
                for s in ["https", "http"]:
                    link = f"{s}://{sub}.{self.target_url}"
                    try:
                        async with session.get(link, timeout=5) as r:
                            if str(r.status) in self.status_codes:
                                self.links.append(link)
                            print(f"[*] Response status :: [{r.status}] links :: {link} Content-length :: {r.content_length}")
                    except:
                        print(f"[*] WARNING :: {link} doesn't exist")
                        continue



if __name__ == "__main__":
    pass
