package week14;

import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.util.Duration;


public class NodeStyleRotateDemoNew extends Application {
    StackPane pane = new StackPane();
    int rotation = 45;
    public void start(Stage primaryStage) {
        // Create a scene and place a button in the scene
        Button btOK = new Button("OK");
        btOK.setStyle("-fx-border-color: blue;");
        //btOK.setRotate(-45);
        pane.getChildren().add(btOK);

        rotate();

        pane.setStyle(
                "-fx-border-color: red; -fx-background-color: lightgray;");

        Scene scene = new Scene(pane, 200, 250);
        primaryStage.setTitle("NodeStyleRotateDemo"); // Set the stage title
        primaryStage.setScene(scene); // Place the scene in the stage
        primaryStage.show(); // Display the stage

        spin();
    }

    public void rotate() {
        rotation += 45;
        rotation %= 360;
        System.out.println("points: "+rotation/45);
        pane.setRotate(rotation);
    }

    public void spin() {

        KeyFrame k = new KeyFrame(Duration.millis(1000), e -> rotate());
        Timeline t = new Timeline(k);
        t.setCycleCount(8);
        t.play();
    }
    /**
     * The main method is only needed for the IDE with limited
     * JavaFX support. Not needed for running from the command line.
     */
    public static void main(String[] args) {
        launch(args);
    }
}

