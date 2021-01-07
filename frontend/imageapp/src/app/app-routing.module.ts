import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {PostdetailsComponent} from "./postdetails/postdetails.component";

const routes: Routes = [
  {path:'detail/:title',component:PostdetailsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
