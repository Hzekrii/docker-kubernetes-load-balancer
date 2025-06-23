import { Routes } from '@angular/router';
import { AuthGuard } from '../auth.guard';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () =>
      import('../components/home/home.component').then((m) => m.HomeComponent),
  },
  // Add other protected routes here
];