package hw4;

import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;
import javafx.util.Duration;

import static javafx.scene.paint.Color.*;


public class ConnectFour extends Application{
    private Circle[][] circles = new Circle[6][7];
    private int[][] numbers = new int[6][7];
    private GridPane gameGrid = new GridPane();
    private boolean redTurn = true;
    private Label condition = new Label("Red player turn");
    private int[][] result;
    private Paint winColor;
    private int turnsLeft = 42;
    private Button newGame = new Button("Play Again?");

    public void start(Stage connectStage){
        gameGrid.setAlignment(Pos.CENTER);
        gameGrid.setHgap(10);
        gameGrid.setVgap(10);

        newGame.setOnMouseClicked(e -> draw());

        draw();

        Scene scene = new Scene(gameGrid,750, 750);
        scene.setFill(DARKBLUE);
        connectStage.setScene(scene);
        connectStage.setTitle("Connect Four");
        connectStage.show();
    }
    public void draw() {
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 7; j++) {
                Circle curCircle = new Circle(40, Color.WHITE);
                curCircle.setStroke(Color.BLUE);

                curCircle.setOnMouseClicked(e -> turn(curCircle));
                circles[i][j] = curCircle;
                numbers[i][j] = 0;
                gameGrid.add(circles[i][j], j, i);

            }
        }
        gameGrid.add(condition, 3 ,7);
    }
    private void turn(Circle curCircle){
        if (turnsLeft > 0){
            if(curCircle.getFill() == Color.WHITE){
               validMove(curCircle);
            }
            else{
                condition.setText("Space is filled");
            }
        }
        else{
            condition.setText("NO WINNERS!");
        }
        result = isConsecutiveFour(numbers);
        if(result != null){ // when someone wins!
            for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 7; j++) {
                    circles[i][j].setOnMouseClicked(null);
                }
            }
            condition.setText("ConnectFour!");
            winColor = circles[result[0][0]][result[0][1]].getFill();
            Timeline ani1 = new Timeline(new KeyFrame(Duration.millis(500), e ->
                    flash(circles[result[0][0]][result[0][1]])));
            Timeline ani2 = new Timeline(new KeyFrame(Duration.millis(500), e ->
                    flash(circles[result[1][0]][result[1][1]])));
            Timeline ani3 = new Timeline(new KeyFrame(Duration.millis(500), e ->
                    flash(circles[result[2][0]][result[2][1]])));
            Timeline ani4 = new Timeline(new KeyFrame(Duration.millis(500), e ->
                    flash(circles[result[3][0]][result[3][1]])));

            ani1.setCycleCount(Timeline.INDEFINITE);
            ani2.setCycleCount(Timeline.INDEFINITE);
            ani3.setCycleCount(Timeline.INDEFINITE);
            ani4.setCycleCount(Timeline.INDEFINITE);

            ani1.play();
            ani2.play();
            ani3.play();
            ani4.play();


            gameGrid.add(newGame, 5, 7);

        }
    }
    public void flash(Circle c){ // makes winning circles flash
        if(c.getFill() == BLUE){
            c.setFill(winColor);
        }
        else{
            c.setFill(BLUE);
        }
    }

    private void validMove(Circle c){
            if (gameGrid.getRowIndex(c) == 5 || numbers[gameGrid.getRowIndex(c) + 1][gameGrid.getColumnIndex(c)] > 0 ){
                if(redTurn){
                    c.setFill(RED);
                    numbers[gameGrid.getRowIndex(c)][gameGrid.getColumnIndex(c)] = 1;
                    redTurn = false;
                    condition.setText("Yellow's turn");
                    turnsLeft -= 1;
                }
                else{
                    c.setFill(YELLOW);
                    numbers[gameGrid.getRowIndex(c)][gameGrid.getColumnIndex(c)] = 2;
                    redTurn = true;
                    condition.setText("Red's turn");
                    turnsLeft -= 1;
                }
            }
            else{
                condition.setText("Invalid Move");
            }

        }

    public static int[][] isConsecutiveFour(int[][] values) {
        int numberOfRows = values.length;
        int numberOfColumns = values[0].length;

        // Check rows
        for (int i = 0; i < numberOfRows; i++) {
            if (isConsecutiveFour(values[i]) != null) {
                int[][] result = new int[4][2];
                result[0][0] = result[1][0] = result[2][0] = result[3][0] = i;
                int k = isConsecutiveFour(values[i]);

                result[0][1] = k; result[1][1] = k + 1;
                result[2][1] = k + 2; result[3][1] = k + 3;

                return result;
            }
        }

        // Check columns
        for (int j = 0; j < numberOfColumns; j++) {
            int[] column = new int[numberOfRows];
            // Get a column into an array
            for (int i = 0; i < numberOfRows; i++)
                column[i] = values[i][j];

            if (isConsecutiveFour(column) != null) {
                int[][] result = new int[4][2];
                result[0][1] = result[1][1] = result[2][1] = result[3][1] = j;
                int k = isConsecutiveFour(column);

                result[0][0] = k; result[1][0] = k + 1;
                result[2][0] = k + 2; result[3][0] = k + 3;

                return result;
            }
        }

        // Check major diagonal (lower part)
        for (int i = 0; i < numberOfRows - 3; i++) {
            int numberOfElementsInDiagonal
                    = Math.min(numberOfRows - i, numberOfColumns);
            int[] diagonal = new int[numberOfElementsInDiagonal];
            for (int k = 0; k < numberOfElementsInDiagonal; k++)
                diagonal[k] = values[k + i][k];

            if (isConsecutiveFour(diagonal) != null) {
                int[][] result = new int[4][2];
                int k = isConsecutiveFour(diagonal);
                result[0][0] = k + i;
                result[1][0] = k + 1 + i;
                result[2][0] = k + 2 + i;
                result[3][0] = k + 3 + i;
                result[0][1] = k;
                result[1][1] = k + 1;
                result[2][1] = k + 2;
                result[3][1] = k + 3;
                return result;
            }
        }

        // Check major diagonal (upper part)
        for (int j = 1; j < numberOfColumns - 3; j++) {
            int numberOfElementsInDiagonal
                    = Math.min(numberOfColumns - j, numberOfRows);
            int[] diagonal = new int[numberOfElementsInDiagonal];
            for (int k = 0; k < numberOfElementsInDiagonal; k++)
                diagonal[k] = values[k][k + j];

            if (isConsecutiveFour(diagonal) != null) {
                int[][] result = new int[4][2];
                int k = isConsecutiveFour(diagonal);
                result[0][0] = k;
                result[1][0] = k + 1;
                result[2][0] = k + 2;
                result[3][0] = k + 3;
                result[0][1] = k + j;
                result[1][1] = k + 1 + j;
                result[2][1] = k + 2 + j;
                result[3][1] = k + 3 + j;
                return result;
            }
        }

        // Check sub-diagonal (left part)
        for (int j = 3; j < numberOfColumns; j++) {
            int numberOfElementsInDiagonal
                    = Math.min(j + 1, numberOfRows);
            int[] diagonal = new int[numberOfElementsInDiagonal];

            for (int k = 0; k < numberOfElementsInDiagonal; k++)
                diagonal[k] = values[k][j - k];

            if (isConsecutiveFour(diagonal) != null) {
                int[][] result = new int[4][2];
                int k = isConsecutiveFour(diagonal);
                result[0][0] = k;
                result[1][0] = k + 1;
                result[2][0] = k + 2;
                result[3][0] = k + 3;
                result[0][1] = j - k;
                result[1][1] = j - k - 1;
                result[2][1] = j - k - 2;
                result[3][1] = j - k - 3;
                return result;
            }
        }

        // Check sub-diagonal (right part)
        for (int i = 1; i < numberOfRows - 3; i++) {
            int numberOfElementsInDiagonal
                    = Math.min(numberOfRows - i, numberOfColumns);
            int[] diagonal = new int[numberOfElementsInDiagonal];

            for (int k = 0; k < numberOfElementsInDiagonal; k++)
                diagonal[k] = values[k + i][numberOfColumns - k - 1];

            if (isConsecutiveFour(diagonal) != null) {
                int[][] result = new int[4][2];
                int k = isConsecutiveFour(diagonal);
                result[0][0] = k + i;
                result[1][0] = k + i + 1;
                result[2][0] = k + i + 2;
                result[3][0] = k + i + 3;
                result[0][1] = numberOfColumns - k - 1;
                result[1][1] = numberOfColumns - (k + 1) - 1;
                result[2][1] = numberOfColumns - (k + 2) - 1;
                result[3][1] = numberOfColumns - (k + 3) - 1;
                return result;
            }
        }

        return null;
    }

    public static Integer isConsecutiveFour(int[] values) {
        for (int i = 0; i < values.length - 3; i++) {
            boolean isEqual = true;
            for (int j = i; j < i + 3; j++) {
                if (values[j] != values[j + 1]) {
                    isEqual = false;
                    break;
                }
                if (values[j] == 0){ //excludes white circles while checking for a win
                    isEqual = false;
                    break;
                }
            }

            if (isEqual) return i;
        }

        return null;
    }

    public static void main(String[] args) {
        launch(args);
    }
}
