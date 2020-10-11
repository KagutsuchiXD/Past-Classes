//add pictures
//scale down on rightclick

package week11.wed;

import javafx.application.*;
import javafx.scene.input.MouseButton;
import javafx.stage.*;
import javafx.scene.*;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.scene.image.*;
import javafx.scene.shape.*;
import javafx.scene.text.*;
import javafx.geometry.*;
import javafx.scene.paint.*;
import java.io.*;
import java.util.*;
import javafx.scene.media.*;

public class PhotoViewer extends Application
{
    public static void main(String[] args)
    {
        launch(args);
    }

    private final String PATH = "C:\\Users\\Public\\Pictures";

    @Override public void start(Stage primaryStage)
    {
        TilePane tile = new TilePane();
        tile.setHgap(20);
        tile.setVgap(20);
        tile.setPadding(new Insets(20));
        tile.setPrefColumns(4);

        File dir = new File(PATH);
        File[] files = dir.listFiles();
        for (File f : files)
        {
            Image img = new Image(f.toURI().toString(),
                    200, 200, true, true);

            ImageView iview = new ImageView(img);
            iview.setFitWidth(200);
            iview.setFitHeight(200);
            iview.setPreserveRatio(true);

            iview.setOnMouseClicked(e ->
            {
                if(e.getButton() == MouseButton.SECONDARY) {
                    iview.setScaleX(1.0);
                    iview.setScaleY(1.0);
                }
                else {
                    iview.setScaleX(2.0);
                    iview.setScaleY(2.0);
                }
                File af = new File(PATH);
                Media media = new Media(af.toURI().toString());

                MediaPlayer mplayer = new MediaPlayer(media);
                mplayer.setAutoPlay(true);
            });

            Text txt = new Text(f.getName());
            txt.setFont(new Font("Times New Roman", 16));

            Region spacer = new Region();

            VBox box = new VBox(10, iview, spacer, txt);
            box.setVgrow(spacer, Priority.ALWAYS);
            box.setAlignment(Pos.CENTER);
            tile.getChildren().add(box);
        }

        ScrollPane scroll = new ScrollPane(tile);
        scroll.setMinWidth(920);
        scroll.setMinHeight(450);

        Scene scene = new Scene(scroll);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Photo Viewer - " + PATH);
        primaryStage.show();
    }

}
