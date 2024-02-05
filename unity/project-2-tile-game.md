Sure, here's a step-by-step guide to create a simple 2D game in Unity:

1. **Create a New Project**
   - Open Unity Hub and click on "New" to create a new 2D project.

2. **Create the Game Board**
   - Create a 10x10 matrix of squares. Each square can be a simple 2D sprite. You can create a prefab for the square and instantiate it in a grid pattern using two nested for loops.

3. **Color the Squares**
   - Create different materials for each color (green, red, white, grey, blue) in the Inspector.
   - Assign these materials to the squares randomly. For the maze, you could use a maze generation algorithm to decide which squares should be grey.

4. **Create the Player**
   - Create a new sprite for the player and give it the blue material.
   - Position the player on one of the squares.

5. **Move the Player**
   - Create a new C# script for the player.
   - In the script, change the player's direction when W/A/S/D is pressed.
   - Move the player one square in the current direction every tick.

Here's a simple example of how the player script might look:

```csharp
public class PlayerScript : MonoBehaviour
{
    public float speed = 1.0f;
    private Vector2 direction = Vector2.zero;

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.W))
            direction = Vector2.up;
        else if (Input.GetKeyDown(KeyCode.A))
            direction = Vector2.left;
        else if (Input.GetKeyDown(KeyCode.S))
            direction = Vector2.down;
        else if (Input.GetKeyDown(KeyCode.D))
            direction = Vector2.right;

        if (Time.time % (1.0f / 4) < 0.01f)  // 4 ticks per second
            transform.Translate(direction * speed);
    }
}
```

6. **Test the Game**
   - Click on the "Play" button at the top of the Unity interface to start playing your game in the Game view.

Remember, this is a very basic version of the game and there's a lot more you can add to it, like interactions between the player and the different types of squares, scoring, etc. Happy coding!

---

## Step 2: Collission detection
To add collision detection in Unity, you can use the built-in physics engine. Here's a step-by-step guide:

1. **Add Collider Components**
   - For the player and the squares, you need to add appropriate collider components. If your player and squares are 2D sprites, you should add a 2D collider (like `BoxCollider2D` or `CircleCollider2D`).

2. **Create a Collision Script**
   - Create a new C# script, you might name it `PlayerCollision`.
   - In this script, you can use the `OnCollisionEnter2D(Collision2D collision)` function to detect when the player has collided with another object.

Here's an example of how the `PlayerCollision` script might look:

```csharp
using UnityEngine;

public class PlayerCollision : MonoBehaviour
{
    void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.tag == "Green")
        {
            // Handle collision with green square
        }
        else if (collision.gameObject.tag == "Red")
        {
            // Handle collision with red square
        }
        // Add more conditions for other square types
    }
}
```

3. **Assign Tags**
   - In Unity, you can assign tags to game objects. Assign appropriate tags (like "Green", "Red", etc.) to your squares.
   - This way, in the `OnCollisionEnter2D` function, you can check the tag of the collided object to determine its type and handle the collision accordingly.

4. **Attach the Script**
   - Finally, attach the `PlayerCollision` script to your player object.

Remember to adjust the code to fit your game's specific needs. For example, you might want to add code to handle the collision differently depending on the type of square the player collided with.

---

## Detecting other types of collissions

In Unity, collision between two game objects can be detected using the built-in physics engine. Here's a step-by-step guide:

1. **Add Collider Components**
   - For the game objects that you want to detect collision between, you need to add appropriate collider components. If your game objects are 2D sprites, you should add a 2D collider (like `BoxCollider2D` or `CircleCollider2D`).

2. **Create a Collision Script**
   - Create a new C# script, you might name it `CollisionScript`.
   - In this script, you can use the `OnCollisionEnter2D(Collision2D collision)` function to detect when the game object has collided with another object.

Here's an example of how the `CollisionScript` script might look:

```csharp
using UnityEngine;

public class CollisionScript : MonoBehaviour
{
    void OnCollisionEnter2D(Collision2D collision)
    {
        Debug.Log("Collided with " + collision.gameObject.name);
    }
}
```

3. **Attach the Script**
   - Finally, attach the `CollisionScript` script to your game objects.

In the `OnCollisionEnter2D` function, `collision.gameObject` is the object that your game object collided with. You can add code in this function to handle the collision as needed for your game.