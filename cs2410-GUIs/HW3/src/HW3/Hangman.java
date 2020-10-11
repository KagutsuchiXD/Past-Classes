package HW3;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.scene.shape.Arc;
import javafx.scene.shape.ArcType;

public class Hangman extends Application {

    @Override
    public void start(Stage hangerStage) throws Exception{
        Circle circle = new Circle(); //make person
        circle.setCenterX(300);
        circle.setCenterY(200);
        circle.setRadius(50);
        circle.setStroke(Color.BLACK);
        circle.setFill(null);

        Line body = new Line(300, 250, 300, 400);
        Line leftArm = new Line(300, 300, 250, 400);
        Line rightArm = new Line(300, 300, 350, 400);
        Line leftLeg = new Line(300, 400, 250, 500);
        Line rightLeg = new Line(300, 400, 350, 500);


        Line noose = new Line(300, 150, 300, 100);// make gallows
        Line gallow = new Line(300, 100, 100, 100);
        Line post = new Line(100, 100, 100, 545);
        Arc stand = new Arc(100, 575, 80, 30, 30, 125);
        stand.setFill(Color.WHITE);
        stand.setType(ArcType.OPEN);
        stand.setStroke(Color.BLACK);


        Pane pane = new Pane();
        pane.getChildren().add(circle);
        pane.getChildren().add(body);

        pane.getChildren().add(noose);
        pane.getChildren().add(gallow);
        pane.getChildren().add(post);
        pane.getChildren().add(stand);
        pane.getChildren().add(leftArm);
        pane.getChildren().add(rightArm);
        pane.getChildren().add(leftLeg);
        pane.getChildren().add(rightLeg);


        Scene scene = new Scene(pane, 500, 650);
        hangerStage.setTitle("Hangman"); // Set the stage title
        hangerStage.setScene(scene); // Place the scene in the stage
        hangerStage.show(); // Display the stage
    }


    public static void main(String[] args) {
        launch(args);
    }
}
