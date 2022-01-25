import { Component, OnInit } from '@angular/core';
import { NgOption } from '@ng-select/ng-select';

import { ApiService } from '../api.service';

@Component({
  selector: 'app-first-form',
  templateUrl: './first-form.component.html',
  styleUrls: ['./first-form.component.scss']
})
export class FirstFormComponent implements OnInit{

    dashboards = [
        {id: 1, value:"lines", name: 'Time Lines'},
        {id: 2, value:"dots", name: 'Time Dots'},
        //{id: 2, value:"bars", name: 'Time Bars'},
        {id: 3, value:"scatter", name: 'Scatter'}
    ];

    selectedDashboard;
    selectedDashboards = [];
    selectedDashboardsXpan = [];
    innerHtml;
    showPlot = false;
    xpanBool = false;

    constructor(private apiService: ApiService) {
    }

    public onSaveXpanChanged(value:boolean){
        this.xpanBool = value;
        this.showPlot = false;
    }

    public addDashboard(params){
      var dashboard = {
         name: this.selectedDashboard,
         params: params
      };
      this.selectedDashboards.push(dashboard);
      this.showPlot = false;
    }

    public deleteDashboard(index: number) {
      this.selectedDashboards.splice(index, 1);
      this.showPlot = false;
    }
    public generate(){
      console.log("generating")
      var xpan = {
         name: "xpan",
         params: this.xpanBool
      };
      //this.selectedDashboardsXpan = { ...this.selectedDashboards };
      this.selectedDashboardsXpan = Object.assign([], this.selectedDashboards);
      this.selectedDashboardsXpan.push(xpan);
      this.apiService.generatePlots(this.selectedDashboardsXpan)
      .subscribe(
         data => {
            this.innerHtml = data;
         },
         error => console.log('There is no plot generated', + error));

      this.showPlot = true;
      console.log("generated")
    }


    ngOnInit(){

    }
}
