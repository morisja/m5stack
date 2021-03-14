#include <M5StickCPlus.h>
const int initial_brightness = 10;

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <unistd.h>

#define PI 3.141
//m5stickc is 80 x 160, the plus is bigger
//plus is 135x240

#define IMG_X 6
#define IMG_Y 6
#define X_MAX 240 - IMG_X - 1
#define Y_MAX 135 - IMG_Y - 1
#define X_MIN 1
#define Y_MIN 1

struct Coord
{
    // actual x and y position
    double x;
    double y;
    //x and y direction +1 for up/right
    int x_dir;
    int y_dir;
    //quantized counters for x and y location
    int x_path;
    int y_path;
};

int is_within_bounds(struct Coord pos)
{
    if (pos.x >= X_MIN && pos.x < X_MAX && pos.y >= Y_MIN && pos.y < Y_MAX)
    {
        return 1;
    }
    return 0;
}

void advance_position(struct Coord *pos, double angle_rads)
{
    pos->x_path = pos->x_path + pos->x_dir;
    pos->y_path = pos->y_path + pos->y_dir;
    pos->x = sin(angle_rads) * pos->x_path;
    pos->y = cos(angle_rads) * pos->y_path;
}
void handle_bounce(struct Coord *pos)
{
    if (pos->y > Y_MAX)
    {
        pos->y = Y_MAX - 1;
        pos->y_dir = -1;
    }
    if (pos->x > X_MAX)
    {
        pos->x = X_MAX - 1;
        pos->x_dir = -1;
    }
    if (pos->y < Y_MIN)
    {
        pos->y = Y_MIN;
        pos->y_dir = 1;
    }
    if (pos->x < X_MIN)
    {
        pos->x = X_MIN;
        pos->x_dir = 1;
    }
}
// Originally I was using fillScreen
// but overwriting the previous image was faster
void hide_rect(struct Coord *pos)
{
    M5.Lcd.fillRect(pos->x, pos->y, IMG_X, IMG_Y, BLACK);
}

void print_rect(struct Coord *pos)
{
    M5.Lcd.fillRect(pos->x, pos->y, IMG_X, IMG_Y, RED);
}


void bounce(void)
{
    double angle_rads = 0.75;

    struct Coord pos;
    pos.x_path = 0;
    pos.y_path = 0;
    pos.x = X_MIN;
    pos.y = Y_MIN;
    pos.x_dir = 1;
    pos.y_dir = 1;

    while (1)
    {
        while (is_within_bounds(pos))
        {
            hide_rect(&pos);
            advance_position(&pos, angle_rads);
            print_rect(&pos);
            delay(10);
        }
        // hide as handle bounce adjusts position
        hide_rect(&pos);
        handle_bounce(&pos);
    }

    return;
}

void setup(void)
{
    M5.begin();
    M5.Lcd.fillScreen(BLACK);
    M5.Lcd.setRotation(1);
    M5.Axp.ScreenBreath(initial_brightness);
}

void loop(void)
{
    bounce();
}
