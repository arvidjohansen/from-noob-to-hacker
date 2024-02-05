
1. **Create a New Project**
   - Open Unity Hub and click on "New" to create a new 2D project.

2. **Create the Paddles**
   - In the Hierarchy window, click on "Create" > "2D Object" > "Sprite" to create a new sprite.
   - Rename this sprite to "Paddle1".
   - In the Inspector window, adjust the size of the sprite to resemble a Paddle.
   - Duplicate "Paddle1" and rename it to "Paddle2".

3. **Create the Ball**
   - Repeat the process above to create a new sprite, but this time name it "Ball" and adjust its size to be smaller.

4. **Add Physics**
   - With the "Ball" selected, in the Inspector window, click on "Add Component" > "Physics 2D" > "Rigidbody 2D".
   - Set the "Gravity Scale" to 0 so the ball doesn't fall down.
   - Click on "Add Component" > "Physics 2D" > "Circle Collider 2D" to add a collider to the ball.
   - Repeat the process for the paddles, but add a "Box Collider 2D" instead.

5. **Create the Scripts**
   - Right-click in the Project window, select "Create" > "C# Script".
   - Name this script "PaddleScript".
   - Double click on it to open the script editor.
   - Write a script to move the paddle up and down when the W/S or Up/Down keys are pressed.
   - Repeat the process to create a "BallScript" to control the ball's movement.

```csharp
// PaddleScript
public float speed = 10.0f;
void Update() {
    if (gameObject.name == "Paddle1") {
        if (Input.GetKey(KeyCode.W)) {
            transform.Translate(new Vector2(0, speed * Time.deltaTime));
        } else if (Input.GetKey(KeyCode.S)) {
            transform.Translate(new Vector2(0, -speed * Time.deltaTime));
        }
    } else if (gameObject.name == "Paddle2") {
        if (Input.GetKey(KeyCode.UpArrow)) {
            transform.Translate(new Vector2(0, speed * Time.deltaTime));
        } else if (Input.GetKey(KeyCode.DownArrow)) {
            transform.Translate(new Vector2(0, -speed * Time.deltaTime));
        }
    }
}

// BallScript
public float speed = 10.0f;
void Start() {
    // Give the ball some initial movement
    GetComponent<Rigidbody2D>().velocity = Vector2.right * speed;
}
```

6. **Attach the Scripts**
   - Drag and drop the "PaddleScript" onto both paddles and the "BallScript" onto the ball in the Hierarchy window.

7. **Test the Game**
   - Click on the "Play" button at the top of the Unity interface to start playing your game in the Game view.

8. **Add Scoring**
   - You can add a scoring system by creating a new UI Text element (right-click in Hierarchy > UI > Text) and updating it whenever the ball hits a boundary.

Remember, this is a very basic version of Pong and there's a lot more you can add to it, like improving the AI, adding sounds, improving the physics, etc. Happy coding!