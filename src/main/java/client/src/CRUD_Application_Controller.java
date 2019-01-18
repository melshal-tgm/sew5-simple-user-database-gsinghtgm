import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicNameValuePair;
import org.json.JSONObject;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;

public class CRUD_Application_Controller {

	@FXML
	private TableColumn<User, String> tablePicture;

	@FXML
	private TableColumn<User, Button> tableAction;

	@FXML
	private TextField inputUsernameField;

	@FXML
	private TableView<User> contentTable;

	@FXML
	private TextField inputPictureField;

	@FXML
	private Button addUser;

	@FXML
	private TableColumn<User, Integer> tableID;

	@FXML
	private Button resetUser;

	@FXML
	private TableColumn<User, String> tableEmail;

	@FXML
	private TextField inputEmailField;

	@FXML
	private TableColumn<User, String> tableUsername;

	private ObservableList<User> tableData = FXCollections.observableArrayList();

	public ArrayList<User> getUsers(String apiUrl) throws Exception {
		ArrayList<User> users = new ArrayList<User>();
		String url = apiUrl;
		URL obj = new URL(url);
		HttpURLConnection con = (HttpURLConnection) obj.openConnection();
		BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
		String inputLine;
		StringBuffer response = new StringBuffer();
		while ((inputLine = in.readLine()) != null) {
			response.append(inputLine);
		}
		in.close();
		JSONObject myResponse = new JSONObject(response.toString());
		JSONObject userjson = myResponse.getJSONObject("users");
		for (int i = 1; i <= userjson.length(); i++) {
			JSONObject user1 = userjson.getJSONObject("user" + i);
			users.add(new User(user1.getString("username"), user1.getString("email"), user1.getString("picture")));

		}
		return users;

	}

	@FXML
	void addNewUser(ActionEvent event) throws ClientProtocolException, IOException {
		if (inputUsernameField.getText().isEmpty() || inputEmailField.getText().isEmpty()
				|| inputPictureField.getText().isEmpty()) {
			System.out.println("IS EMPTY");
		} else {

			HttpClient httpclient = HttpClients.createDefault();
			HttpPost httppost = new HttpPost("http://localhost:5000/users");
			// Request parameters and other properties.
			List<NameValuePair> params = new ArrayList<NameValuePair>(2);
			params.add(new BasicNameValuePair("username", inputUsernameField.getText()));
			params.add(new BasicNameValuePair("email", inputEmailField.getText()));
			params.add(new BasicNameValuePair("picture", inputPictureField.getText()));
			httppost.setEntity(new UrlEncodedFormEntity(params, "UTF-8"));
			// Execute and get the response.
			HttpResponse response = httpclient.execute(httppost);
			showUsers();
		}
	}

	@FXML
	void resetCreateNewUser(ActionEvent event) {
		inputUsernameField.clear();
		inputEmailField.clear();
		inputPictureField.clear();
	}

	public void showUsers() {
		tableUsername.setCellValueFactory(new PropertyValueFactory<>("username"));
		tableEmail.setCellValueFactory(new PropertyValueFactory<>("email"));
		tablePicture.setCellValueFactory(new PropertyValueFactory<>("picture"));
		// contentTable.setItems(tableData);
		try {
			tableData = FXCollections.observableArrayList(getUsers("http://localhost:5000/users"));
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		contentTable.setItems(tableData);

	}

	@FXML
	public void initialize() {
		showUsers();
	}

}