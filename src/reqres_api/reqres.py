import requests
from requests.exceptions import HTTPError
import inspect


def get_resource(path=None):
    url = "https://reqres.in/api"
    if path:
        arg = get_var_name(path)[1]

        if arg == "userId":
            url = f"{url}/users/{path}"

        if arg == "page":
            url = f"{url}/users?page={path}"

        if arg == "resourceId":
            url = f"{url}/unknown/{path}"
    else:
        url = f"{url}/unknown"

    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        resp.raise_for_status()

    except HTTPError as err:
        return (err.response.status_code, err.response.reason)


def create_user(user=None, userId=None):
    func_name = get_var_name(user)[0]

    url = "https://reqres.in/api"

    if func_name in ["create_users"]:
        url = f"{url}/user"

    if func_name in ["update_user", "patch_user", "delete_user"]:
        url = f"{url}/users/{userId}"

    if func_name == "register":
        url = f"{url}/register"

    if func_name == "login":
        url = f"{url}/login"

    try:
        if func_name in ["create_users", "register"]:
            resp = requests.post(url, json=user)

        if func_name in ["update_user", "patch_user"]:
            resp = requests.put(url, json=user)

        if func_name == "delete_user":
            resp = requests.delete(url)

        if func_name == "login":
            resp = requests.post(url, json=user)
        if resp.status_code in [200, 201]:
            return resp.json()

        if resp.status_code == 204:
            return {"Message": f"User has been successfully deleted"}
        resp.raise_for_status()

    except HTTPError as err:
        return (err.response.status_code, err.response.reason)


def get_var_name(path):
    """
    I use this function to retrieve the function name from which it was called
    along with the actual name of the variable used when we call the function.
    """
    # Get the frame object for this function call
    thisframe = inspect.currentframe()

    # Get the parent calling frames details
    frames = inspect.getouterframes(thisframe)

    # Function this function was just called from that we wish to find
    # the calling parameter name for
    func_name = frames[2][3]

    # Get all the details of that functions call including its arguments
    args = inspect.getargvalues(frames[2][0])

    arg = args.args[0]

    return [func_name, arg]
