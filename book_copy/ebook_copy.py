import pyautogui as auto
import time
import pyperclip

#북큐브
total_page =392
book_name='부의 추월 차선'
capture_pos=(245,117)
ebook_screen_center_pos=(515,606)
ebook_screen_right_pos=(907,502)
sleep_time =0.5

for i in range(int(total_page)):
    file_name = book_name + '_'+ str(i+1).zfill(4) + '.png'
    pyperclip.copy(file_name)

    auto.click(capture_pos)
    time.sleep(sleep_time)

    #auto.click(ebook_screen_center_pos)
    #time.sleep(sleep_time)

    auto.hotkey('ctrl','v')
    time.sleep(sleep_time)
    
    auto.press('enter')
    time.sleep(sleep_time)
    
    auto.click(ebook_screen_right_pos)
    time.sleep(sleep_time)

    