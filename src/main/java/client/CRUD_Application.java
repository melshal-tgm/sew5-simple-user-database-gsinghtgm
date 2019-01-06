package client;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class CRUD_Application extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("LoginPage_css.fxml"));
        primaryStage.setTitle("CRUD Application");
        primaryStage.setScene(new Scene(root, 800, 500));
        primaryStage.show();r
    }


    public static void main(String[] args) {
        launch(args);
    }
}