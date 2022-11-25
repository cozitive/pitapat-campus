import React from "react";
import { Provider } from "react-redux";
import { MemoryRouter, Routes, Route } from "react-router-dom";
import { ToolkitStore } from "@reduxjs/toolkit/dist/configureStore";
import { render, screen } from "@testing-library/react";
import ChatList from "../../page/ChatList";
import { getDefaultMockStore } from "../../test-utils/mocks";
import paths from "../../constant/path";


const mockNavigate = jest.fn();
jest.mock("react-router-dom", () => ({
  ...jest.requireActual("react-router-dom"),
  useNavigate: () => mockNavigate,
}));


describe("ChatList", () => {
  function getElement(store: ToolkitStore) {
    return (
      <Provider store={store}>
        <MemoryRouter>
          <Routes>
            <Route path={"/"} element={<ChatList />} />
            <Route path={paths.signIn} element={<div>sign in</div>} />
          </Routes>
        </MemoryRouter>
      </Provider>
    );
  }


  it("should be rendered", () => {
    render(getElement(getDefaultMockStore()));
  });

  it("should redirect if there is no login user",  () => {
    render(getElement(getDefaultMockStore(false)));
    const signInPage = screen.getByText("sign in");
    expect(signInPage).toBeInTheDocument();
  });
});
