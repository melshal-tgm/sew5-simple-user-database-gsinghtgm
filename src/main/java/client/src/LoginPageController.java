import java.io.IOException;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class LoginPageController {
	@FXML
	public TextField apiAdressField;

	@FXML
	private TextField usernameField;

	@FXML
	private Button loginButton;

	@FXML
	private TextField passwordField;

	@FXML
	void login(ActionEvent event) {
		try {
			Node node = (Node) event.getSource();
			Stage stage = (Stage) node.getScene().getWindow();
			Parent root = FXMLLoader.load(getClass().getResource("CRUD_Application_css.fxml"));
			Scene scene = new Scene(root);
			stage.setScene(scene);
			stage.show();

			stage.setX((1366 - stage.getWidth()) / 2);
			stage.setY((728 - stage.getHeight()) / 2);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
