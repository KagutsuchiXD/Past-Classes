package hw5;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Arc;
import javafx.scene.shape.ArcType;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.stage.Stage;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class Hangman extends Application {
    private char[] alphabet =  "abcdefghijklmnopqrstuvwxyz".toCharArray();
    private ArrayList<String> phrases = new ArrayList<>();
    private Label directions = new Label("Pick a letter");
    private int wrongs = 0;
    private String gamePhrase;
    private Button replay = new Button("Play Again");
    private ArrayList<Button> bList = new ArrayList<>();
    private int corCounter = 0;

    //hangman parts
    private Circle head = new Circle(); //make person
    private Line body = new Line(300, 250, 300, 400);
    private Image byu = new Image(
            "http://www.byustore.com/site/product_images/65845+Logo+Products+Lg+Decal+9_main-1.jpg",
            50, 50, false, false);
    private ImageView pin = new ImageView(byu);
    private Line leftArm = new Line(300, 300, 250, 400);
    private Line rightArm = new Line(300, 300, 350, 400);
    private Line leftLeg = new Line(300, 400, 250, 500);
    private Line rightLeg = new Line(300, 400, 350, 500);


    private Line noose = new Line(300, 150, 300, 100);// make gallows
    private Line gallows = new Line(300, 100, 100, 100);
    private Line post = new Line(100, 100, 100, 545);
    private Arc stand = new Arc(100, 575, 80, 30, 30, 125);

    private Label announcement = new Label();
    private GridPane hangerPane;

    public void start(Stage hangerStage) throws Exception{
        hangerPane = playBoard();
        final Scene[] scene = {new Scene(hangerPane, 1100, 600)};
        replay.setOnAction(e -> {
            try{
                hangerPane = playBoard();
                scene[0] = new Scene(hangerPane, 1100, 600);
                hangerStage.setScene(scene[0]);
            } catch(FileNotFoundException fe){
                System.err.println("FileNotFound");
            }
        });



        hangerStage.setTitle("Hangman"); // Set the stage title
        hangerStage.setScene(scene[0]); // Place the scene in the stage
        hangerStage.show(); // Display the stage
    }

    private GridPane playBoard() throws FileNotFoundException{
        GridPane playPane = new GridPane();
        playPane.setHgap(50);
        playPane.setVgap(50);

        //make hangman screen
        Pane hangManPane = makeHangman();

        //options menu
        GridPane options = new GridPane();
        options.setHgap(50);
        options.setVgap(50);
        Scanner file = new Scanner(new FileReader("phrases.txt"));
        while(file.hasNext()){
            String phrase = file.nextLine();
            phrases.add(phrase);
        }
        gamePhrase = phrases.get((int)(Math.random()* phrases.size()));
        char[] gPhrase = gamePhrase.toCharArray();

        options.add(new Label("Use the letters to guess the phrase below."),0 , 0);
        options.add(directions, 0, 1);
        options.add(makeLetterBoard(alphabet, gPhrase), 0, 2);
        options.add(announcement,0,3);
        options.add(replay,0, 5);
        replay.setVisible(false);

        //put it all together
        playPane.add(options, 0, 0);
        playPane.add(hangManPane, 3,0);
        //playPane.setColumnSpan(hangManPane, 500);

        return playPane;
    }
    private Pane makeHangman(){
        //hangman screen
        head.setCenterX(300);
        head.setCenterY(200);
        head.setRadius(50);
        head.setStroke(null);
        head.setFill(null);
        body.setStroke(null);
        leftArm.setStroke(null);
        rightArm.setStroke(null);
        leftLeg.setStroke(null);
        rightLeg.setStroke(null);
        pin.setX(275);
        pin.setY(275);
        pin.setVisible(false);

        stand.setFill(null);
        stand.setType(ArcType.OPEN);
        stand.setStroke(Color.BLACK);


        Pane hPane = new Pane();
        hPane.getChildren().add(head);
        hPane.getChildren().add(body);

        hPane.getChildren().add(noose);
        hPane.getChildren().add(gallows);
        hPane.getChildren().add(post);
        hPane.getChildren().add(stand);
        hPane.getChildren().add(leftArm);
        hPane.getChildren().add(rightArm);
        hPane.getChildren().add(leftLeg);
        hPane.getChildren().add(rightLeg);
        hPane.getChildren().add(pin);
        return hPane;
    }
    // functions for options
    private GridPane makeLetterBoard(char[] options, char[] phrase) {
        announcement.setText("Let the Games begin!");
        GridPane lBoard = new GridPane();
        lBoard.setHgap(3);
        lBoard.setVgap(7);

        ArrayList<TextField> letters = new ArrayList<>();
        int r = 0;
        int c = 0;
        for (char o : options) {
            Button letter = new Button(Character.toString(o)); //buttons for guessing letters
            letter.setOnAction(e -> turn(letter, letters));
            letter.setPrefWidth(30);
            bList.add(letter);
            if(c < 13){
                lBoard.add(letter, c, r);
                c++;
            }
            else{
                r++;
                c = 0;
                lBoard.add(letter, c, r);
                c++;
            }
        }

        int pc = 0;
        int pr = 9;
        for (char l : phrase){
            if(l != ' '){
                TextField gpLetter = new TextField(Character.toString(l)); // textfields show the message as you go
                gpLetter.setEditable(false);
                letters.add(gpLetter);
                gpLetter.setPrefWidth(30);
                gpLetter.setStyle("-fx-text-fill: white;");
                lBoard.add(gpLetter, pc, pr);
            }
            else{
                if(pc >= 12){
                    pc = 0;
                    pr++;
                }
            }
            pc++;
        }
        return lBoard;
    }
    private void turn(Button letter, ArrayList<TextField> letters){
        if(corCounter == letters.size()){
            announcement.setText("You won!");
            announcement.setTextFill(Color.BLUE);
            for (Button b : bList){
                b.setOnAction(null);
            }
            replay.setVisible(true);
        }
        else{
            String ref = letter.getText();
            letter.setOnAction(null);
            letter.setText(" ");
            if (gamePhrase.toLowerCase().contains(ref)){
                announcement.setText("Correct!");
                announcement.setTextFill(Color.GREEN);
                // make all of this letter in string visible
                for(TextField t : letters){
                    if(ref.equals(t.getText().toLowerCase())){
                        t.setStyle("-fx-text-fill: black;");
                        corCounter ++;
                    }
                }
            }
            else{
                announcement.setText("Incorrect!");
                announcement.setTextFill(Color.RED);
                switch (wrongs){
                    case 0:
                        head.setStroke(Color.BLACK);
                        wrongs++;
                        break;
                    case 1:
                        body.setStroke(Color.BLACK);
                        pin.setVisible(true);
                        wrongs++;
                        break;
                    case 2:
                        leftArm.setStroke(Color.BLACK);
                        wrongs++;
                        break;
                    case 3:
                        rightArm.setStroke(Color.BLACK);
                        wrongs++;
                        break;
                    case 4:
                        leftLeg.setStroke(Color.BLACK);
                        wrongs++;
                        break;
                    case 5:
                        rightLeg.setStroke(Color.BLACK);
                        for (Button b : bList){
                            b.setOnAction(null);
                        }
                        wrongs = 0;
                        corCounter = 0;
                        announcement.setText("Poor Hangman, you lost.\nBetter luck next time.");
                        replay.setVisible(true);
                        break;
                }
            }
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
