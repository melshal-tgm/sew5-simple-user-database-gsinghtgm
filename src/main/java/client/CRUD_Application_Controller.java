package client;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.control.TableView;
import javafx.scene.control.TableColumn;
import javafx.event.ActionEvent;
import javafx.collections.ObservableList;
import javafx.collections.FXCollections;

public class CRUD_Application_Controller {

    @FXML
    private TableColumn<String, String> tablePicture;

    @FXML
    private TableColumn<String, String> tableAction;

    @FXML
    private TextField inputUsernameField;

    @FXML
    private TableView<String> contentTable;

    @FXML
    private TextField inputPictureField;

    @FXML
    private Button addUser;

    @FXML
    private TableColumn<String, String> tableID;

    @FXML
    private Button resetUser;

    @FXML
    private TableColumn<String, String> tableEmail;

    @FXML
    private TextField inputEmailField;

    @FXML
    private TableColumn<String, String> tableUsername;

    private ObservableList<String> tableData = FXCollections.observableArrayList(("test"));

    @FXML
    void addNewUser(ActionEvent event) {
        contentTable.setItems(tableData);
    }

    @FXML
    void resetCreateNewUser(ActionEvent event) {

    }
}