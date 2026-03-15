import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/')({
  component: App,
  loader: async ({ context }) => {
    const data = await context.queryClient.ensureQueryData(
      context.trpc.todos.list.queryOptions(),
    )
    return data
  },
})

function App() {
  const todos = Route.useLoaderData()
  console.log(todos)
  return (
    <main className="page-wrap px-4 pb-8 pt-14">
      <h2 className="text-center text-4xl font-semibold">
        Welcome to <span className="text-slate-500">somaspace</span>{' '}
      </h2>
    </main>
  )
}
