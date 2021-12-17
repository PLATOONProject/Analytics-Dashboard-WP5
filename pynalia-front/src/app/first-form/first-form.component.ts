import { Component, OnInit } from '@angular/core';
import { NgOption } from '@ng-select/ng-select';

@Component({
  selector: 'app-first-form',
  templateUrl: './first-form.component.html',
  styleUrls: ['./first-form.component.scss']
})
export class FirstFormComponent {

    dashboards = [
        {id: 1, value:"lines", name: 'Time Lines', avatar: '//www.gravatar.com/avatar/b0d8c6e5ea589e6fc3d3e08afb1873bb?d=retro&r=g&s=30 2x'},
        {id: 2, value:"dots", name: 'Time Lines & Dots', avatar: '//www.gravatar.com/avatar/ddac2aa63ce82315b513be9dc93336e5?d=retro&r=g&s=15'},
        {id: 3, value:"scatter", name: 'Time Lines & Scatter', avatar: '//www.gravatar.com/avatar/6acb7abf486516ab7fb0a6efa372042b?d=retro&r=g&s=15'}
    ];

    selectedDashboard;
    selectedDashboards = [];

    constructor() {
    }

    onAddDashboard(column){
      var dashboard = {
         name: this.selectedDashboard,
         column: column
      };
      this.selectedDashboards.push(dashboard);
    }

    generate(){
      alert(this.selectedDashboards.length)
    }
}
