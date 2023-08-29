from setup_app.setting.config import settings
from setup_app.browser.chrome_browser import chrome_browser

chrome_browser.move_url(settings.TARGET_URL)

chrome_browser.click_element(
    element='/html/body/div[2]/div[1]/div[1]/div/div/div/div/header/div/div/div[4]/div[2]/div/a/div/div[1]', option='xpath')  # 버튼 클릭

chrome_browser.input_text_filed(
    element='/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]', text=settings.LOGIN_ID, option='xpath')  # id 입력

chrome_browser.input_text_filed(
    element='/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input', text=settings.LOGIN_PASSWORD, option='xpath')  # password 입력

chrome_browser.click_element(
    element='/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input', option='xpath')  # 로그인 상태 유지 아니요 버튼

chrome_browser.click_element(
    element='/html/body/div[3]/div[1]/div[1]/div/button', option='xpath')  # 버튼 클릭

chrome_browser.click_link_tag(
    element='/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div[7]/span/a/div[2]/span', option='link_text')  # a 링크로 이동


if __name__ == '__main__':
    input()
