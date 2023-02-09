from playwright.sync_api import Page
import config
import qase


class IndexPage:
    _BUTTON_GOOGLE_SEARCH = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"
    _LINK_ENGLISH_LANG = "//a[contains(text(), 'English')]"

    @qase.step(
        action='Open the Index page',
        data=config.url.DOMAIN,
        expected_result='The page opened'
    )
    def open_index_page(self, page: Page) -> None:  # noqa
        page.goto(config.url.DOMAIN)

    @qase.step(
        action='Press the English Language link',
        expected_result='The page language changed to English'
    )
    def press_link_english_lang(self, page: Page):
        page.locator(self._LINK_ENGLISH_LANG).click()

    @qase.step(
        action='Check the text in the Google Search button',
        expected_result='The test is equal Google Search'
    )
    def get_text_from_google_search_button(self, page: Page) -> None:
        return page.locator(self._BUTTON_GOOGLE_SEARCH).get_attribute('value')
