package ch.unine.iiun.safecloud;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;

@RestController
public class Controller {

    private Store store;

    @Autowired
    public void setStore(Store store) {
        this.store = store;
    }

    @RequestMapping(value="/{path}", method = RequestMethod.GET)
    public ResponseEntity<byte[]> get(@PathVariable String path) {
        byte[] data = {};
        try {
            data = this.store.get(path);
            return new ResponseEntity<byte[]>(data, HttpStatus.OK);
        } catch (MissingResourceException e) {
            return new ResponseEntity<byte[]>(data, HttpStatus.NOT_FOUND);
        } catch (IOException e) {
            return new ResponseEntity<byte[]>(data, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @RequestMapping(value="/{path}", method = RequestMethod.PUT)
    public ResponseEntity<String> put(@PathVariable String path, @RequestBody byte[] body) {
        try {
            this.store.put(path, body);
            return new ResponseEntity<String>(path, HttpStatus.OK);
        } catch (IOException e) {
            return new ResponseEntity<String>(path, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
