package hw6;

import javafx.animation.RotateTransition;
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
import javafx.scene.paint.ImagePattern;
import javafx.scene.shape.*;
import javafx.scene.text.Font;
import javafx.stage.Stage;
import javafx.util.Duration;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class WheelofFortune extends Application {
    private char[] alphabet =  "abcdefghijklmnopqrstuvwxyz".toCharArray();
    private ArrayList<String> phrases = new ArrayList<>();
    private Label directions = new Label("Pick a letter");
    private String gamePhrase;
    private Button replay = new Button("Play Again");
    private ArrayList<Button> bList = new ArrayList<>();
    private int corCounter = 0;
    private int score = 0;
    private Label scoreid = new Label("Your Score is: ");
    private Label scoreAmount = new Label();

    //wheel parts
    private File pic = new File("wheel2.png");
    private Circle wheel = new Circle(250, 300, 200);
    private Polygon pointer = new Polygon(50, 200, 5, 200, 25, 160);
    private Button spin = new Button("Spin!");
    private Boolean spun;
    private int angle = 0;

    private Label announcement = new Label();
    private GridPane fortunePane;

    public void start(Stage wheelStage) throws Exception{
        fortunePane = playBoard();
        final Scene[] scene = {new Scene(fortunePane, 1200, 550)};
        replay.setOnAction(e -> {
            try{
                fortunePane = playBoard();
                scene[0] = new Scene(fortunePane, 1200, 550);
                wheelStage.setScene(scene[0]);
            } catch(FileNotFoundException fe){
                System.err.println("FileNotFound");
            }
        });



        wheelStage.setTitle("Wheel of Fortune!"); // Set the stage title
        wheelStage.setScene(scene[0]); // Place the scene in the stage
        wheelStage.show(); // Display the stage
    }

    private GridPane playBoard() throws FileNotFoundException{
        GridPane playPane = new GridPane();
        playPane.setHgap(50);
        playPane.setVgap(50);

        //make hangman screen
        Pane wheelPane = makeWheelBoard();

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
        playPane.add(wheelPane, 3,0);
        //playPane.setColumnSpan(hangManPane, 500);

        return playPane;
    }
    private Pane makeWheelBoard(){
        //wheel screen
        score = 0;
        scoreAmount.setText(" ");
        scoreid.setLayoutX(200);
        scoreid.setLayoutY(50);
        scoreAmount.setLayoutX(300);
        scoreAmount.setLayoutY(50);
        pointer.setFill(Color.RED);
        wheel.setFill(new ImagePattern(new Image(pic.toURI().toString())));
        spun = false;
        spin.setLayoutX(30);
        spin.setPrefWidth(75);
        spin.setLayoutY(450);
        spin.setPrefHeight(50);
        spin.setVisible(true);
        spin.setOnAction(e ->{
            if(!spun){
                int panelNum = (int)(Math.random() * 8);
                int temp = (panelNum * 45) + 1080;
                angle += temp;
                angle %=360;
                RotateTransition rotate = new RotateTransition(Duration.millis(2000), wheel);
                rotate.setByAngle(temp);
                rotate.play();
                switch(angle){
                    case 0:
                        score += 300;
                        break;
                    case 45:
                        score += 800;
                        break;
                    case 90:
                        score += 200;
                        break;
                    case 135:
                        score += 600;
                        break;
                    case 180:
                        score += 400;
                        break;
                    case 225:
                        score += 500;
                        break;
                    case 270:
                        score += 100;
                        break;
                    case 315:
                        score += 700;
                        break;
                }
                spun = true;
                spin.setVisible(false);
            }
        });


        Pane wPane = new Pane();

        wPane.getChildren().add(wheel);
        wPane.getChildren().add(pointer);
        wPane.getChildren().add(spin);
        wPane.getChildren().add(scoreid);
        wPane.getChildren().add(scoreAmount);
        return wPane;
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

       if(spun){
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
                   announcement.setText("Correct! Spin the Wheel!");
                   announcement.setTextFill(Color.GREEN);
                   scoreAmount.setText(Integer.toString(score));
                   spun = false;
                   spin.setVisible(true);
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
                   spun = false;
                   spin.setVisible(true);
                   score = 0;
                   scoreAmount.setText("0");

               }
           }
       }
       else{
           announcement.setText("Please spin the wheel before guessing another letter.");
       }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
