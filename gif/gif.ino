#include <M5StickC.h>
#include "img.h"

const int initial_brightness=10;

void setup(void) {
    M5.begin();
    pinMode(M5_BUTTON_HOME, INPUT);
    M5.Lcd.fillScreen(BLACK);
    M5.Lcd.setRotation(1);
    M5.Axp.ScreenBreath(initial_brightness);
}

void loop(void) {

    for (int i=0; i<19; i++){
        M5.Lcd.pushImage(  0,0,111,80, (uint16_t *)spongebob[i]);
        delay(50);
    }


}
