//x Bindings, dynamic updates
//play around with bind() functions
//play around with set functions

//Friday add Color, section 14.5
// https://docs.oracle.com/javase/8/javafx/api/javafx/scene/paint/Color.html

package week4.fri;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

public class ShowCircleCentered extends Application {
    @Override // Override the start method in the Application class
    public void start(Stage primaryStage) {
        // Create a pane to hold the circle
        Pane pane = new Pane();
        // Create a circle and set its properties
        Circle circle = new Circle();
        circle.centerXProperty().bind(pane.widthProperty().divide(2));
        circle.centerYProperty().bind(pane.heightProperty().divide(2));
        circle.setRadius(50);


        Color col = new Color(0.25, 0.14, 0.333, 0.51);
        Color col3 = Color.web("#0F2439");//AggieBlue
        circle.setStroke(Color.BLACK);
        //circle.setFill(col);

        Color col2 = new Color(0.5, 0.25, 0.0, 1.0);
        circle.setFill(col3);
        //circle.setStroke(Color.BLACK);
        //circle.setFill(Color.WHITE);
        pane.getChildren().add(circle); // Add circle to the pane

        // Create a scene and place it in the stage
        Scene scene = new Scene(pane, 200, 200);
        primaryStage.setTitle("ShowCircleCentered"); // Set the stage title
        primaryStage.setScene(scene); // Place the scene in the stage
        primaryStage.show(); // Display the stage
    }

    /**
     * The main method is only needed for the IDE with limited
     * JavaFX support. Not needed for running from the command line.
     */
    public static void main(String[] args) {
        launch(args);
    }
}