import requests

class BaseService:
    def _request(self, url: str, method: str = "GET", body=None, custom_headers=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        if custom_headers:
            headers.update(custom_headers)

        options = {
            "headers": headers
        }

        if body is not None:
            content_type = headers.get("Content-Type", "")
            if "application/x-www-form-urlencoded" in content_type:
                options["data"] = body
            elif isinstance(body, (dict, list)):
                options["json"] = body
            elif isinstance(body, str):
                options["data"] = body
            else:
                options["data"] = body

        try:
            response = requests.request(method, url, **options)
            if response.status_code < 200 or response.status_code >= 300:
                raise Exception(f"API request failed with status {response.status_code}: {response.reason}")
            
            if not response.text:
                return {}

            try:
                return response.json()
            except ValueError:
                return response.text
        except Exception as error:
            # Re-throw or format the error professionally
            raise Exception(f"[IslamicContentSdk] {str(error)}")
