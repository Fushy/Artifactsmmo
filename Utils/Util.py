import inspect
from collections.abc import Iterable
from datetime import timedelta
from time import sleep
from typing import Callable

import pyperclip

from Times import now


# pip install --upgrade
# pip install --upgrade pip
# pip install --upgrade pip setuptools
# pip install numpy
# pip install telegram
# pip install python-telegram-bot --upgrade
# pip install ffmpeg-python
# pip install pydub
# pip install selenium
# pip install msedge-selenium-tools
# pip install http-request-randomizer


# TODO verif type
# if type(browser).__name__ != WebDriver.__name__ and type(browser).__name__ != WebElement.__name__:
#     error_text = "\tget_text_selector browser is not a good type {} {}".format(type(browser), WebDriver, WebElement)
#     if debug: print(error_text)
#     raise ValueError(error_text)


def current():
    print("Current file:", inspect.currentframe().f_code.co_filename)
    # print("Current fun:", inspect.stack(1)[0].function)
    print("Current fun:", inspect.currentframe().f_code.co_name)
    print("Current line:", inspect.currentframe().f_lineno)


def current_file():
    return inspect.currentframe().f_code.co_filename


def is_iter(element):
    if isinstance(element, Iterable):
        return True
    return False


def know_connected_wifi_password():
    """netsh
    wlan
    show
    profiles
    "MAIS_MAROL"
    key = clear"""


def infinite_sequence():
    num = 0
    while True:
        num += 1
        yield num


def chained_list(*args):
    """ A utiliser lorsqu'il n'y a pas d'effet de bord
    :param args:
    :return:
    """
    while True:
        for element in args:
            yield element


def loop_screenshot(browser):
    while True:
        screenshot(browser)
        sleep(0.1)


def screenshot(browser, file=""):
    if file == "":
        file = now().strftime("%d-%m-%y %H-%M-%S %Z")
    # save_browser = copy.deepcopy(browser)
    save_browser = browser
    print("screenshot", now().strftime("%d-%m-%y %H-%M-%S %Z"))
    for i in range(len(save_browser.window_handles)):
        save_browser.switch_to.window(save_browser.window_handles[i])
        print("\tscreenshots\\" + file + "_" + str(i) + ".png")
        save_browser.get_screenshot_as_file("screenshots\\" + file + "_" + str(i) + ".png")


def util_action_on_one_clipboard_change(fun: Callable):
    old_clipboard = ""
    while True:
        clipboard = pyperclip.paste()
        if clipboard != old_clipboard:
            fun(clipboard)
        old_clipboard = clipboard
        sleep(1)


def sorted_dict(dictionary: dict, key=lambda x: x, reverse=False) -> str:
    result = "{"
    v_is_dict = False
    for k, v in sorted(dictionary.items(), key=key, reverse=reverse):
        if type(v) is dict:
            v_is_dict = True
            v = sorted_dict(v)
        elif type(v) is Iterable:
            v = sorted(v)
        k = str(k)
        if v_is_dict is False:
            v = str(v)
            if v.isalnum() or v.isalpha() or v.isidentifier() or v.isascii():
                result += "\"" + k + "\":\"" + v + "\","
            else:
                result += "\"" + k + "\":" + v + ","
        else:
            v = str(v)
            if v.isalnum() or v.isalpha() or v.isidentifier():
                result += "\"" + k + "\":\"" + v + "\","
            else:
                result += "\"" + k + "\":" + v + ","
    result = list(result)
    result[-1:] = "}"
    return "".join(result)


def util_repeat_function_binance(fun: Callable, interval_time: timedelta, debug=False, *args):
    """ Une fois que la fonction est terminée, on attend :interval_time:."""
    while True:
        fun()
        if debug:
            print(now().strftime("%Y-%m-%d %H:%M:%S"), "executed successfully", *args)
        sleep(interval_time.total_seconds())

# def set_bag_alienworlds(browser, tool_name):
#     """ Doit  au préalable être connecté """
#     left_interface_xpath = "/html/body/div/div[3]/div[1]/div/div[2]/button"
#     wait_n_click(browser, left_interface_xpath)
#     switch_tools_xpath = "/html/body/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/div[2]/button"
#     wait_n_click(browser, switch_tools_xpath)
#     sleep(1)
#     tools_xpath = list(
#         "/html/body/div/div[3]/div[2]/div[2]/div/div/div/div/div/div[3]/div[2]/div[{}]".format(i) for i in range(1,
#         4))
#     tools = list(map(lambda x: get_element(browser, x), tools_xpath))
#     last_tool = get_element(browser, "/html/body/div/div[3]/div[2]/div[2]/div/div/div/div/div/div[3]/div[2]/div[3]")
#     while last_tool:
#         advenced_tds = get_all_tag_that_contains(last_tool, [lambda x: tool_name == x], alone=True)
#         if advenced_tds is None or len(advenced_tds) != 0:
#             break
#         else:
#             element_click(browser, last_tool)
#         advenced_tds = get_all_tag_that_contains(last_tool, [lambda x: tool_name == x], alone=True)
#         if advenced_tds is None or len(advenced_tds) == 0:
#             continue
#         element_click(browser, advenced_tds[tool_name])
#         check_wax_approve(browser)
#         sleep(1)
#         last_tool = get_element(browser, "/html/body/div/div[3]/div[2]/div[2]/div/div/div/div/div/div[3]/div[
#         2]/div[3]")
#     return True
#
#
# def set_bag_waxblocks(browser, to, ids: list[int]):
#     try:
#         print("set_bag", to, ids)
#         if not whitelist_wam_account(to):
#             raise ValueError("Wam account is not whitelisted")
#         search_account_input_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/form/div/input"
#         search_account_input = get_element(browser, search_account_input_xpath)
#         account_name = "m.federation"
#         waxblocks_connection(browser, False)
#         clear_send(search_account_input)
#         element_send(search_account_input, account_name, Keys.ENTER)
#         contract_tab_xpath = "/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]"
#         if not wait_n_click(browser, contract_tab_xpath):
#             say("change VPN connection")
#             return False
#         action_tab_xpath = "/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]"
#         if not wait_n_click(browser, action_tab_xpath):
#             say("change VPN connection")
#             return False
#         setbag_onglet_xpath = "/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[4]/div/div/div/div/div/span[17]"
#         if not wait_n_click(browser, setbag_onglet_xpath):
#             say("change VPN connection")
#             return False
#         to_account_xpath = "/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[4]/div/div/div/div[2]/div/div[
#         1]/div/div/input"
#         to_account = get_element(browser, to_account_xpath)
#         clear_send(to_account)
#         element_send(to_account, to, Keys.TAB, "[" + ",".join(map(str, ids)) + "]")
#         sleep(1)
#         submit_xpath = "/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[4]/div/div/div/div[2]/button"
#         if not wait_n_click(browser, submit_xpath):
#             say("change VPN connection")
#             return False
#         sleep(5)
#         if not check_wax_approve(browser):
#             close_current_and_go_home(browser)
#             return True
#         message_transaction_xpath = "/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[4]/div/div/div/div[3]/div"
#         if not wait_element(browser, message_transaction_xpath, leave=10):
#             return False
#         message_transaction_text = get_text(browser, message_transaction_xpath)
#         print("\tmessage set_bag", message_transaction_text)
#         if "Error" == message_transaction_text:
#             return False
#         return True
#     except StaleElementReferenceException:
#         return set_bag_waxblocks(browser, to, ids)
#
#
