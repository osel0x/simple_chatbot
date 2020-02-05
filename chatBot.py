from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os
from checkSiteTemperature import checkSiteTemperature


def test():
    text_box.send_keys("It works!!!\n")


if os.name == 'nt':  # Windows
    os.chdir('E:/oselox/projects/Include/Driver')
    print(os.getcwd())
    path = os.getcwd()
elif os.name == 'posix':  # MACOSX
    print(os.getcwd)
    os.chdir('/Users/oselox/projects/Include/Driver')
    print(os.getcwd())
    path = os.getcwd()
else:  # Mainly Linux
    print(os.getcwd)
    os.chdir('/home/oselox/projects/Include/Driver')
    print(os.getcwd())
    path = os.getcwd()

filepath = 'whatsapp_session.txt'
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        if cnt == 0:
            executor_url = line
        if cnt == 1:
            session_id = line


def create_driver_session(session_id, executor_url):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    RemoteWebDriver.execute = org_command_execute

    return new_driver


driver2 = create_driver_session(session_id, executor_url)
print("Driver 2 URL: " + driver2.current_url)

# A dictionary that stores all the users with permissions to activate bot
bot_users = {
    "Contact1": True,
    "Contact2": True,
}

# A dictionary that stores those users that the bot already indicated them how to activate it
bot_users_notification = {
    "Contact1": None,
    "Contact2": None,
}

# A dictionary of unauthorized and banned users
unauthorized_bot_users = {}

while True:
    wait = WebDriverWait(driver2, 600)
    # Green dot for new messages
    unread = driver2.find_elements_by_class_name("P6z4j")
    # Area to write messages
    text_box = driver2.find_element_by_class_name("_3u328")
    name, message = '', ''
    if len(unread) > 0:
        ele = unread[-1]
        action = webdriver.common.action_chains.ActionChains(driver2)
        action.move_to_element_with_offset(ele, 0, -20)  # move a bit to the left from the green dot
        # Clicking couple of times because sometimes whatsapp web responds after two clicks
        try:
            action.click()
            action.perform()
            action.click()
            action.perform()
        except Exception as e:
            pass
        try:
            # Contact name
            name = driver2.find_element_by_class_name("_19vo_")
            # Instructions for out bot
            message = driver2.find_elements_by_class_name("_F7Vk")[-1]
            if name.text in bot_users:
                if bot_users[name.text]:
                    message = driver2.find_elements_by_class_name("_F7Vk")[-1]
                    if 'show' in message.text.lower() and 'projects' in message.text.lower():
                        test()
                    if 'show' in message.text.lower() and 'site' in message.text.lower() and 'temp' in message.text.lower():
                        site_temp = checkSiteTemperature()
                        text_box = driver2.find_element_by_class_name("_3u328")
                        response = "Internal Sensor:" + site_temp[0] + "\nExternal Sensor:" + site_temp[1] + "\n"
                        text_box.send_keys(response)
                    if 'activate bot' in message.text.lower():
                        if name.text.lower() not in bot_users:
                            bot_users[name] = True
                            text_box = driver2.find_element_by_class_name("_3u328")
                            response = "Hi " + name.text + "Oselox's Bot activated for you\n" \
                                                           "How can I help you:\n" \
                                                           "Show projects\n" \
                                                           "Show Site Temp\n" \
                                                           "Deactivate\n" \
                                                           "Write your full text for your selection:\n"
                            text_box.send_keys(response)
                            # sleep(2)
                    if 'deactivate' in message.text.lower():
                        if name.text in bot_users:
                            if bot_users[name.text]:
                                text_box = driver2.find_element_by_class_name("_3u328")
                                response = "Bye " + name.text + ".\n"
                                text_box.send_keys(response)
                                bot_users[name.text] = None
                                bot_users_notification[name.text] = None
                    else:
                        if not bot_users_notification[name.text]:
                            text_box = driver2.find_element_by_class_name("_3u328")
                            response = "Please start with >>>Activate bot<<< command\nThanks\n"
                            text_box.send_keys(response)
                            bot_users_notification[name.text] = True
                else:
                    if not bot_users_notification[name.text]:
                        text_box = driver2.find_element_by_class_name("_3u328")
                        response = "Please start with >>>Activate bot<<< command\nThanks\n"
                        text_box.send_keys(response)
                        bot_users_notification[name.text] = True
            else:
                if name.text not in unauthorized_bot_users:
                    text_box = driver2.find_element_by_class_name("_3u328")
                    unauthorized_bot_users[name.text] = True
                    # response = "Unauthorized User:" + name.text + ".\n"
                    response = ""
                    text_box.send_keys(response)
        except Exception as e:
            print(e)
            pass
    else:
        try:
            name = driver2.find_element_by_class_name("_19vo_")  # Contact name
            message = driver2.find_elements_by_class_name("_F7Vk")[-1]  # the message content
            if name.text in bot_users:
                if bot_users[name.text]:
                    message = driver2.find_elements_by_class_name("_F7Vk")[-1]
                    if 'show' in message.text.lower() and 'projects' in message.text.lower():
                        test()
                    if 'show' in message.text.lower() and 'site' in message.text.lower() and 'temp' in message.text.lower():
                        site_temp = checkSiteTemperature()
                        text_box = driver2.find_element_by_class_name("_3u328")
                        response = "Internal Sensor:" + site_temp[0] + "\nExternal Sensor:" + site_temp[1] + "\n"
                        text_box.send_keys(response)
                    if 'activate bot' in message.text.lower():
                        if name.text.lower() not in bot_users:
                            bot_users[name.text] = True
                            text_box = driver2.find_element_by_class_name("_3u328")
                            response = "Hi " + name.text + "Oselox's Bot activated for you\n" \
                                                           "How can I help you:\n" \
                                                           "Show projects\n" \
                                                           "Show Site Temp\n" \
                                                           "Deactivate\n" \
                                                           "Write your full text for your selection:\n"
                            text_box.send_keys(response)
                            # sleep(2)
                    if 'deactivate' in message.text.lower():
                        if name.text in bot_users:
                            if bot_users[name.text]:
                                text_box = driver2.find_element_by_class_name("_3u328")
                                response = "Bye " + name.text + ".\n"
                                text_box.send_keys(response)
                                bot_users[name.text] = None
                                bot_users_notification[name.text] = None
                    else:
                        if not bot_users_notification[name.text]:
                            text_box = driver2.find_element_by_class_name("_3u328")
                            response = "Please start with >>>Activate bot<<< command\nThanks\n"
                            text_box.send_keys(response)
                            bot_users_notification[name.text] = True
                else:
                    if not bot_users_notification[name.text]:
                        text_box = driver2.find_element_by_class_name("_3u328")
                        response = "Please start with >>>Activate bot<<< command\nThanks\n"
                        text_box.send_keys(response)
                        bot_users_notification[name.text] = True
            else:
                if name.text not in unauthorized_bot_users:
                    text_box = driver2.find_element_by_class_name("_3u328")
                    unauthorized_bot_users[name.text] = True
                    # response = "Unauthorized User:" + name.text + ".\n"
                    response = ""
                    text_box.send_keys(response)
        except Exception as e:
            print(e)
            pass
    sleep(2)
