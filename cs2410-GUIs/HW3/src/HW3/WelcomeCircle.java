package HW3;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;

import static javafx.scene.paint.Color.BLACK;


public class WelcomeCircle extends Application {
    public void start(Stage phraseStage) throws Exception{
        String phrase = "Welcome to Java!";
        Pane pane = new Pane();

        Circle base = new Circle();
        base.setCenterX(200);
        base.setCenterY(200);
        base.setRadius(100);
        base.setFill(null);
        base.setStroke(null);

        int index = 0;
        double degree = 360 / phrase.length();
        for (double degrees = 0; index < phrase.length(); index++, degrees += degree) {
            double pointX = base.getCenterX() + base.getRadius() *
                    Math.cos(Math.toRadians(degrees));
            double pointY = base.getCenterY() + base.getRadius() *
                    Math.sin(Math.toRadians(degrees));
            Text letter = new Text(pointX, pointY, phrase.charAt(index) + " ");
            letter.setFill(Color.CRIMSON);
            letter.setFont(Font.font("Verdana", 25));
            letter.setRotate(degrees + 90);
            pane.getChildren().add(letter);
        }


        Scene scene = new Scene(pane, 400, 400);
        phraseStage.setTitle("Circular Text Display"); // Set the stage title
        phraseStage.setScene(scene); // Place the scene in the stage
        phraseStage.show(); // Display the stage
    }
    public static void main(String[] args) {
        launch(args);
    }
}
