import os
import concurrent.futures
import httpx
from Tool import Tool
from utils import Utils

class CookieChecker(Tool):
    def __init__(self, app):
        super().__init__("Cookie Checker", "Checks if cookies are valid and shuffle and unduplicate them.", 1, app)

        self.cache_file_path = os.path.join(self.cache_directory, "verified-cookies.txt")

    def run(self):
        cookies = self.get_cookies()

        if self.config["delete_invalid_cookies"]:
            f = open(self.cache_file_path, 'w')
            f.seek(0)
            f.truncate()

        working_cookies = 0
        failed_cookies = 0
        total_cookies = len(cookies)

        # for each line, test the proxy
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.config["max_workers"]) as self.executor:
            results = [self.executor.submit(self.test_cookie, cookie, self.config["use_proxy"]) for cookie in cookies]

            for future in concurrent.futures.as_completed(results):
                try:
                    is_working, cookie, response_text = future.result()
                except Exception as e:
                    is_working, response_text = False, str(e)

                if is_working:
                    working_cookies += 1
                else:
                    failed_cookies += 1

                if self.config["delete_invalid_cookies"] and is_working:
                    f.write(cookie + "\n")
                    f.flush()

                self.print_status(working_cookies, failed_cookies, total_cookies, response_text, is_working, "Working")

        if self.config["delete_invalid_cookies"]:
            f.close()
            os.replace(self.cache_file_path, self.cookies_file_path)

    @Utils.retry_on_exception(2)
    def test_cookie(self, cookie, use_proxy):
        """
        Checks if a cookie is working
        """
        proxies = self.get_random_proxies() if use_proxy else None

        with httpx.Client(proxies=proxies) as client:
            user_agent = self.get_random_user_agent()
            req_url = "https://www.roblox.com/mobileapi/userinfo"
            req_cookies = { ".ROBLOSECURITY": cookie }
            req_headers = self.get_roblox_headers(user_agent)

            response = client.get(req_url, headers=req_headers, cookies=req_cookies)

            if response.status_code != 200:
                raise Exception(Utils.return_res(response))

            result = response.json()

            user_id = result["UserID"]
            username = result["UserName"]
            robux_balance = result["RobuxBalance"]

        return True, cookie, f"UserID: {user_id} | Username: {username} | Robux Balance: {robux_balance}"
