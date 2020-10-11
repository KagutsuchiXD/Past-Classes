package HW3;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class TwoRectangles extends Application{

    private Label directions1 = new Label("Input the x and y center positions");
    private Label directions2 = new Label("as well as width and height");

    private TextField rec1x = new TextField();
    private Label r1x = new Label("Rectangle 1 x-position");
    private TextField rec1y = new TextField();
    private Label r1y = new Label("Rectangle 1 y-position");
    private TextField rec1w = new TextField();
    private Label r1w = new Label("Rectangle 1 width");
    private TextField rec1h = new TextField();
    private Label r1h = new Label("Rectangle 1 height");

    private TextField rec2x = new TextField();
    private Label r2x = new Label("Rectangle 2 x-position");
    private TextField rec2y = new TextField();
    private Label r2y = new Label("Rectangle 2 y-position");
    private TextField rec2w = new TextField();
    private Label r2w = new Label("Rectangle 2 width");
    private TextField rec2h = new TextField();
    private Label r2h = new Label("Rectangle 2 height");
    private Button show = new Button("Show Rectangles");

    private Rectangle rec1 = new Rectangle();
    private Rectangle rec2 = new Rectangle();
    private Label conclusion = new Label(".....");


    public void start(Stage rectangleStage) throws Exception{

        GridPane textGrid = new GridPane(); // input pane
        textGrid.setPadding(new Insets(50, 50, 50, 50));
        textGrid.setStyle("-fx-border-color: red");
        textGrid.setHgap(10);
        textGrid.setVgap(10);


        textGrid.add(directions1, 0, 0);
        textGrid.add(directions2, 1, 0);
        textGrid.add(r1x, 0, 1);
        textGrid.add(r1y, 0, 2);
        textGrid.add(r1w, 0, 3);
        textGrid.add(r1h, 0, 4);
        textGrid.add(rec1x, 1, 1);
        textGrid.add(rec1y, 1, 2);
        textGrid.add(rec1w, 1, 3);
        textGrid.add(rec1h, 1, 4);

        textGrid.add(r2x, 0, 6);
        textGrid.add(r2y, 0, 7);
        textGrid.add(r2w, 0, 8);
        textGrid.add(r2h, 0, 9);
        textGrid.add(rec2x, 1, 6);
        textGrid.add(rec2y, 1, 7);
        textGrid.add(rec2w, 1, 8);
        textGrid.add(rec2h, 1, 9);
        textGrid.add(show, 1, 10);

        Pane recPane = new Pane();
        show.setOnAction(e -> createRectangles());
        rec1.setFill(null);
        rec1.setStroke(Color.CRIMSON);
        rec2.setFill(null);
        rec2.setStroke(Color.NAVY);
        recPane.getChildren().addAll(rec1, rec2);

        textGrid.add(recPane, 4, 1, 30, 30);
        textGrid.add(conclusion, 4, 2);
        Scene scene = new Scene(textGrid, 1000, 600);
        rectangleStage.setTitle("Two Rectangles");
        rectangleStage.setScene(scene);
        rectangleStage.show();

    }

    private void createRectangles(){
        int true1w = Integer.parseInt(rec1w.getText());
        int true1h = Integer.parseInt(rec1h.getText());
        int true1x = Integer.parseInt(rec1x.getText()) - (true1w/2);
        int true1y = Integer.parseInt(rec1y.getText()) - (true1h/2);

        rec1.setX(true1x);
        rec1.setY(true1y);
        rec1.setWidth(true1w);
        rec1.setHeight(true1h);

        int true2w = Integer.parseInt(rec2w.getText());
        int true2h = Integer.parseInt(rec2h.getText());
        int true2x = Integer.parseInt(rec2x.getText()) - (true2w/2);
        int true2y = Integer.parseInt(rec2y.getText())- (true2h/2);

        rec2.setX(true2x);
        rec2.setY(true2y);
        rec2.setWidth(true2w);
        rec2.setHeight(true2h);

        if((true1x > true2x && true1y > true2y && (true1x + true1w) > (true2x + true2w) && (true1y + true1h) > (true2y + true2h)) ||
                (true2x > true1x && true2y > true1y && (true2x + true2w) > (true1x + true1w) && (true2y + true2h) > (true1y + true1h))){
            conclusion.setText("One Rectangle is contained in another!");
        }
        else if((true1x >= true2x && true1y >= true2y && true1x <= (true2x + true2w) && true1y <= (true2y + true2h)) || //r1 in bottom right of r2
                (true1x >= true2x && (true1y + true1h) >= true2y && true1x <= (true2x + true2w) && (true1y + true1y) <= (true2y + true2h)) || // r1 in top right of r2
                ((true1x + true1w) >= true2x && (true1y + true1h) >= true2y && (true1x + true1w) <= (true2x + true2w) && (true1y + true1h) <= (true2y + true2h)) || // r1 in top left of r2
                ((true1x + true1w) >= true2x && true1y >= true2y && (true1x + true1w) <= (true2x + true2w) && true1y <= (true2y + true2h))){   // r1 in bottom left of r2
            conclusion.setText("The Rectangles overlap!");

        }
        else if((true2x >= true1x && true2y >= true1y && true2x <= (true1x + true1w) && true2y <= (true1y + true1h)) || //r1 in bottom right of r2
                (true2x >= true1x && (true2y + true2h) >= true1y && true2x <= (true1x + true1w) && (true2y + true2y) <= (true1y + true1h)) || // r1 in top right of r2
                ((true2x + true2w) >= true1x && (true2y + true2h) >= true1y && (true2x + true2w) <= (true1x + true1w) && (true2y + true2h) <= (true1y + true1h)) || // r1 in top left of r2
                ((true2x + true2w) >= true1x && true2y >= true1y && (true2x + true2w) <= (true1x + true1w) && true2y <= (true1y + true1h))){   // r1 in bottom left of r2
            conclusion.setText("The Rectangles overlap!");

        }
        else{
            conclusion.setText("The Rectangles do not overlap.");
        }

    }

    public static void main(String[] args) {
        launch(args);
    }
}
