import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;

public class User {

    private final SimpleIntegerProperty id;
    private static int counter = 0;
    private SimpleStringProperty username;
    private SimpleStringProperty email;
    private SimpleStringProperty picture;

    public User(String username, String email, String picture) {
    	this.id=new SimpleIntegerProperty(counter++);
        this.username = new SimpleStringProperty(username);
        this.email = new SimpleStringProperty(email);
        this.picture = new SimpleStringProperty(picture);
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
}