from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "HUESOS V BANKE"}
    # Define speed of the animation in millis
speed = 25

# Define smileys to display
smiley1 = "^_^"
smiley2 = "~_~"
smiley3 = "o.o"
smiley4 = "O.o"

# Function to draw a smiley face
def draw_smiley(smiley_num):
    print(smiley1)
    print(smiley2)
    print(smiley3)
    return

# Main program loop
for i in range(10, 1000, speed):
    draw_smiley(i % 4)
    time.sleep(speed)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

