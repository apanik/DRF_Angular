import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-postdetails',
  templateUrl: './postdetails.component.html',
  styleUrls: ['./postdetails.component.css']
})
export class PostdetailsComponent implements OnInit {
title : any;
info : any;

  constructor(
    private route:ActivatedRoute, private http :HttpClient
  ) { }
  ngOnInit() {
    this.title = this.route.snapshot.params['title']
    this.getOne();
  }
getOne(){
return this.http.get('http://127.0.0.1:8000/detail/'+this.title).subscribe((data)=>{
  this.info = data;
})
}
}
