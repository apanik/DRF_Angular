import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title : string;
  image: string[] = [];
   info: any;
  constructor(private http :HttpClient) {
  }
  onTitleChanged(event : any){
    this.title = event.target.value;
  }
  onImageChanged(event : any){
    for (var i = 0; i < event.target.files.length; i++) {
            this.image.push(event.target.files[i]);
        }
}


  onButtonClicked(){
    const uploadData = new FormData();
      uploadData.append('title',this.title)
      for (var i = 0; i < this.image.length; i++) {
      uploadData.append("image", this.image[i]);
      this.http.post('http://127.0.0.1:8000/post/',uploadData).subscribe((data)=>{
        this.info = data;
      });
    }

    // this.getOne();
  }
  // getOne(){
  //   let data = this.http.get('http://127.0.0.1:8000/post/').subscribe((data)=>{
  //     this.info = data;
  //   });

}
