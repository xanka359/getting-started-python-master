from selene import browser, be, have


browser.open('https://www.ecosia.org/')
browser.element('[name="q"]').should(be.blank).type('a tree is cool').press_enter()
browser.element('[data-test-id="entity-description"]').should(have.text('In botany, a tree is a perennial'))
#if browser.element(by.text('Accept all')).matching(be.visible):
 #  browser.element(by.text('Accept all')).click()