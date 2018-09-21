import { Component, OnInit } from '@angular/core';
import { ApiService } from  '../api.service';

@Component({
  selector: 'app-app-list',
  templateUrl: './app-list.component.html',
  styleUrls: ['./app-list.component.css']
})
export class AppListComponent implements OnInit {

  private apps: Array<object> = [];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getApps();
  }

  public getApps(){
    this.apiService.getApps().subscribe((data: Array<object>) => {
      this.apps = data;
      console.log(data);
    })
  }

}
