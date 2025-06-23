import { Injectable } from '@angular/core';
import { jwtDecode } from 'jwt-decode';
import { Apollo } from 'apollo-angular';
import { LOGIN_MUTATION, REGISTER_MUTATION } from './packages/graphql/graphql.operations';
import { Router } from '@angular/router';

interface TokenPayload {
  user_id: string;
  username: string;
  exp: number;
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor(private apollo: Apollo, private router: Router) {}

  async login(username: string, password: string): Promise<boolean> {
    try {
      const result: any = await this.apollo.mutate({
        mutation: LOGIN_MUTATION,
        variables: { input: { username, password } },
      }).toPromise();

      const token = result?.data?.login?.token;
      if (token) {
        localStorage.setItem('token', token);
        return true;
      }
      return false;
    } catch (error) {
      console.error('Login error:', error);
      return false;
    }
  }

  async register(username: string, password: string, email?: string): Promise<boolean> {
    try {
      const result: any = await this.apollo.mutate({
        mutation: REGISTER_MUTATION,
        variables: { input: { username, password, email } },
      }).toPromise();

      const token = result?.data?.register?.token;
      if (token) {
        localStorage.setItem('token', token);
        return true;
      }
      return false;
    } catch (error) {
      console.error('Registration error:', error);
      return false;
    }
  }

  logout(): void {
  if (typeof window !== 'undefined') {
    localStorage.removeItem('token');
  }
  this.router.navigate(['/login']);
}

  getToken(): string | null {
  if (typeof window === 'undefined') return null;
  return localStorage.getItem('token');
}

  isAuthenticated(): boolean {
    const token = this.getToken();
    if (!token) return false;

    try {
      const decoded = jwtDecode<TokenPayload>(token);
      return decoded.exp * 1000 > Date.now();
    } catch {
      return false;
    }
  }

  getCurrentUser(): TokenPayload | null {
    const token = this.getToken();
    if (!token) return null;

    try {
      return jwtDecode<TokenPayload>(token);
    } catch {
      return null;
    }
  }
}
