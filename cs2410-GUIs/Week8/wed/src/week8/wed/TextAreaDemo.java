package week8.wed;

//2
//Discuss DescriptionPanes
//add event to reset all text
//goto ComboBoxDemo

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.image.ImageView;

public class TextAreaDemo extends Application {

    private DescriptionPane descriptionPane;
    @Override // Override the start method in the Application class
    public void start(Stage primaryStage) {
        // Declare and create a description pane
        descriptionPane = new DescriptionPane();

        // Set title, text and image in the description pane
        descriptionPane.setTitle("Canada");
        String description = "The Canadian national flag ...";
        descriptionPane.setImageView(new ImageView("https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Flag_of_Canada.svg/255px-Flag_of_Canada.svg.png"));
        descriptionPane.setDescription(description);

        //reset all text
        descriptionPane.setOnMouseClicked(e-> getPaneText());

        // Create a scene and place it in the stage
        Scene scene = new Scene(descriptionPane, 450, 200);
        primaryStage.setTitle("TextAreaDemo"); // Set the stage title
        primaryStage.setScene(scene); // Place the scene in the stage
        primaryStage.show(); // Display the stage
    }

    //method to reset all text
    public void getPaneText() {
        System.out.println("getPaneText");
        descriptionPane.setDescription("new Text");
    }
    /**
     * The main method is only needed for the IDE with limited
     * JavaFX support. Not needed for running from the command line.
     */
    public static void main(String[] args) {
        launch(args);
    }
}
