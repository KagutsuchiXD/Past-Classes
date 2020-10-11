package com.company;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.layout.FlowPane;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.stage.Stage;
import javafx.scene.text.*;

public class HelloWorld extends Application{
    public void start(Stage helloStage) throws Exception {
        helloStage.setTitle("Hello World");

        Pane helloPane = new Pane();
        helloPane.setPadding(new Insets(5, 5, 5, 5));

        Scene helloScene = new Scene(helloPane, 500, 300);

        Text word1 = new Text(100, 100, "Hello");
        word1.setFill(Color.BLACK);
        word1.setFont(Font.font("sans serif",FontWeight.BOLD, 50));
        helloPane.getChildren().add(word1);

        Text word2 = new Text(150, 200, "World");
        word2.setFill(Color.CRIMSON);
        word2.setFont(Font.font("joker", FontWeight.BOLD, FontPosture.ITALIC, 55));
        helloPane.getChildren().add(word2);

        helloStage.setScene(helloScene);
        helloStage.show();

    }

    public static void main(String[] args) {
        Application.launch(args);
    }
}
