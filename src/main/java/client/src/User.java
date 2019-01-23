import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpDelete;
import org.apache.http.impl.client.HttpClients;

import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.scene.control.Button;

public class User {

	private SimpleIntegerProperty id;
	private SimpleStringProperty username;
	private SimpleStringProperty email;
	private SimpleStringProperty picture;
	private Button deleteButton;
	private Button editButton;

	public User(CRUD_Application_Controller controller, int id, String username, String email, String picture) {
		this.id = new SimpleIntegerProperty(id);
		this.username = new SimpleStringProperty(username);
		this.email = new SimpleStringProperty(email);
		this.picture = new SimpleStringProperty(picture);
		this.editButton = new Button("Edit");
		this.deleteButton = new Button("Delete");
		editButtonAction(controller);
		deleteButtonAction(controller);
	}

	private void deleteButtonAction(CRUD_Application_Controller controller) {
		this.deleteButton.setOnAction(e -> {
			try {
				HttpClient httpclient = HttpClients.createDefault();
				HttpDelete httpDelete = new HttpDelete("http://localhost:5000/users/user" + this.id.get());
				httpDelete.setHeader("Accept", "application/json");
				httpclient.execute(httpDelete);
				controller.showUsers();
			} catch (Exception ex) {
				ex.printStackTrace();
			}
		});
	}

	private void editButtonAction(CRUD_Application_Controller controller) {
		this.editButton.setOnAction(e -> {
			try {
				System.out.println("hello");
			} catch (Exception ex) {
				ex.printStackTrace();
			}
		});
	}

	public String getEmail() {
		return email.get();
	}

	public void setEmail(String email) {
		this.email = new SimpleStringProperty(email);
	}

	public String getPicture() {
		return picture.get();
	}

	public void setPicture(String picture) {
		this.picture = new SimpleStringProperty(picture);
	}

	public String getUsername() {
		return username.get();
	}

	public void setUsername(String username) {
		this.username = new SimpleStringProperty(username);
	}

	public int getId() {
		return id.get();
	}

	public void setId(int id) {
		this.id = new SimpleIntegerProperty(id);
	}

	public Button getDeleteButton() {
		return deleteButton;
	}

	public void setDeleteButton(Button deleteButton) {
		this.deleteButton = deleteButton;
	}

	public Button getEditButton() {
		return editButton;
	}

	public void setEditButton(Button editButton) {
		this.editButton = editButton;
	}

}