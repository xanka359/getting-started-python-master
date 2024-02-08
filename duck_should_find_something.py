from selene import browser, be, have


browser.open('https://duckduckgo.com/')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="r1-0"]').should(have.text('Selene - GitHub Pages'))
#if browser.element(by.text('Accept all')).matching(be.visible):
 #  browser.element(by.text('Accept all')).click()