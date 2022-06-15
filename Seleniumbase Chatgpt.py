from seleniumbase import SB


with SB(cft=True, uc=True) as sb:
        sb.activate_cdp_mode("https://chatgpt.com/")
        sb.sleep(1)
        sb.click_if_visible('button[aria-label="Close dialog"]')
        sb.click_if_visible('button[data-testid="close-button"]')
        sb.show_file_choosers()
        sb.choose_file("input[type='file']", r"D:\aa.png")
        sb.type("div#prompt-textarea p", "The captcha has 3x3 grid which are in rows starting from top left corner. the first row from left to right direction has 0 1 2. 1st row 1st column is 0, 1st row 2nd column is 1 and 1st row 3rd column is 2.then in same way from left to right direction 2nd row 1st column is 3, 2nd row 2nd column is 4, 2nd row 3rd column is 5 . and then in same way from left to right direction 3rd row 1st column is 6, 3rd row 2nd column is 7, 3rd row 3rd column is 8. Now analyze each box 1 by 1 and store answer. if you think any box contains a faded similar digits.  Analyze it deeply first and then.make a decision. and then select it according to that decision made. Rethink and Reconsider boxes numbers and then give me answer after thinking twice. now solve and in last line give me numbers only answer. Do your progress and thinking and take your time. Just answer without commas and dashes and spaces and anything in last line separate.")
        sb.wait_for_element_not_visible("circle") #This will make sure picture is uploaded
        sb.click('button#composer-submit-button')
        sb.wait_for_element_not_visible('button[data-testid="stop-button"]', timeout=20)
        answer = sb.execute_script("""
        return (() => {
          const msgs = Array.from(
            document.querySelectorAll('div[data-message-author-role="assistant"]')
          );
          if (!msgs.length) return "";
          const lastMsg = msgs[msgs.length - 1];
          const ps = Array.from(lastMsg.querySelectorAll('p'));
          if (!ps.length) return "";
          const lastLine = ps[ps.length - 1].innerText.trim();
          return (lastLine.match(/\\d+/g) || []).join('');
        })();
        """)
        print(f"Extracted answer: {answer}")
        sb.sleep(2)
        
# OR if chat
        # chat = sb.find_element('[data-message-author-role="assistant"] .markdown')
        # soup = sb.get_beautiful_soup(chat.get_html()).text.strip()
        # soup = soup.replace("\n\n\n", "\n\n")
        # print("*** Response from ChatGPT: ***\n%s" % soup)
        # sb.sleep(2)
        
        
        
        
   