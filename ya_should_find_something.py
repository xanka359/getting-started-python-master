from selene import browser, be, have


browser.open('https://ya.ru')
browser.element('[name="text"]').should(be.blank).type('Python').press_enter()
browser.element('[accesskey="1"]').should(have.text('The official home of the'))