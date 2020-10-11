package week9.wed;


import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.beans.property.DoubleProperty;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.util.Duration;

public class BallPane extends Pane {
    public final double radius = 20;
    private double x = radius, y = radius;
    private double dx = 1, dy = 1;
    private Circle circle = new Circle(x, y, radius);
    private Circle hole = new Circle(x,y, radius);
    private Timeline animation;

    public BallPane() {
        circle.setFill(Color.GREEN); // Set ball color
        hole.setFill(Color.BLACK);

        hole.setCenterX(200);
        hole.setCenterY(200);

        getChildren().addAll(circle, hole); // Place a ball into this pane


        // Create an animation for moving the ball
        animation = new Timeline(
                new KeyFrame(Duration.millis(50), e -> moveBall()));
        animation.setCycleCount(Timeline.INDEFINITE);
        animation.play(); // Start animation

        this.setOnMouseClicked(e-> changeBall());
    }

    public void play() {
        animation.play();
    }

    public void pause() {
        animation.pause();
    }

    public void increaseSpeed() {
        animation.setRate(animation.getRate() + 0.1);
    }

    public void decreaseSpeed() {
        animation.setRate(
                animation.getRate() > 0 ? animation.getRate() - 0.1 : 0);
    }

    public DoubleProperty rateProperty() {
        return animation.rateProperty();
    }

    protected void moveBall() {
        // Check boundaries
        if (x < radius || x > getWidth() - radius) {
            dx *= -1; // Change ball move direction
        }
        if (y < radius || y > getHeight() - radius) {
            dy *= -1; // Change ball move direction
        }
        if(circle.getCenterX() == hole.getCenterX() && circle.getCenterY() == hole.getCenterY()){
            dx = 0;
            dy = 0;
        }
        if(circle.getCenterX() >= hole.getCenterX() - hole.getRadius() &&
                circle.getCenterX() <= hole.getCenterX() + hole.getRadius() &&
                circle.getCenterY() >= hole.getCenterY() - hole.getRadius() &&
                circle.getCenterX() <= hole.getCenterX() + hole.getRadius()){
            dx = 0;
            dy = 0;
        }

        // Adjust ball position
        x += dx;
        y += dy;
        circle.setCenterX(x);
        circle.setCenterY(y);
    }

    protected void changeBall() {
        //ADD CLICK LOGIC
    }
}