import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';


import { AppListComponent } from './app-list/app-list.component';
import { AppCreateComponent } from './app-create/app-create.component';

const routes: Routes = [
  
    { path: '', redirectTo: 'apps', pathMatch: 'full' },
    {
      path: 'apps',
      component: AppListComponent
    },
    {
      path: 'create-app',
      component: AppCreateComponent      
    }
  ];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
  })
  export class AppRoutingModule { }